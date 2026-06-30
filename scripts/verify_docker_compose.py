#!/usr/bin/env python3
"""Validate Docker Compose stack without requiring a full manual run (Phase 6)."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REQUIRED_FILES = (
    "docker-compose.yml",
    "Dockerfile",
    "frontend/Dockerfile",
    "pyproject.toml",
    "requirements.txt",
    "frontend/package.json",
    "frontend/next.config.ts",
)

REQUIRED_SERVICES = ("backend", "frontend", "redis", "postgres")


def _static_checks(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"missing_file:{rel}")

    compose_path = root / "docker-compose.yml"
    if compose_path.exists():
        compose = yaml.safe_load(compose_path.read_text(encoding="utf-8")) or {}
        services = compose.get("services") or {}
        for name in REQUIRED_SERVICES:
            if name not in services:
                errors.append(f"missing_service:{name}")
        for name in ("backend", "frontend"):
            if name in services and "healthcheck" not in services[name]:
                errors.append(f"missing_healthcheck:{name}")

    next_config = (root / "frontend/next.config.ts").read_text(encoding="utf-8")
    if "standalone" not in next_config:
        errors.append("frontend_next_config_missing_standalone")

    return errors


def _docker_checks(root: Path) -> dict:
    docker = shutil.which("docker")
    if not docker:
        return {"docker_available": False, "compose_config_ok": None, "note": "Docker CLI not installed"}

    result = subprocess.run(
        [docker, "compose", "-f", str(root / "docker-compose.yml"), "config"],
        capture_output=True,
        text=True,
        cwd=root,
        check=False,
    )
    return {
        "docker_available": True,
        "compose_config_ok": result.returncode == 0,
        "compose_stderr": result.stderr.strip() or None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Docker Compose configuration")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("output/docker_compose_validation.json"))
    args = parser.parse_args()

    root = args.root.resolve()
    static_errors = _static_checks(root)
    docker_info = _docker_checks(root)

    passed = not static_errors and (
        not docker_info["docker_available"] or docker_info.get("compose_config_ok") is True
    )
    report = {
        "passed": passed,
        "static_errors": static_errors,
        **docker_info,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
