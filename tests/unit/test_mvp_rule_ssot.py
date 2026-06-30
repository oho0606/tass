"""MVP Rule SSOT verification tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MVP_CONFIG = ROOT / "config" / "mvp_operational_rules.yaml"


def _mvp_rule_count() -> int:
    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    return sum(len(cfg.get(key, [])) for key in keys)


def test_mvp_config_lists_26_rules() -> None:
    assert _mvp_rule_count() == 26


def test_mvp_rules_have_ssot_files() -> None:
    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    rule_ids = [rid for key in keys for rid in cfg.get(key, [])]

    for rule_id in rule_ids:
        folder = ROOT / "rule_database" / "rules" / rule_id
        assert folder.is_dir(), f"missing folder {rule_id}"
        for name in ("metadata.json", "specification.md", "README.md", "changelog.md"):
            assert (folder / name).exists(), f"{rule_id} missing {name}"


def test_verify_rule_ssot_script_passes() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_rule_ssot.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
