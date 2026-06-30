"""Load MVP rules with lifecycle stage Adopted for production scoring."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import yaml

MVP_CONFIG_PATH = Path("config/mvp_operational_rules.yaml")
RULE_DB_DIR = Path("rule_database/rules")


def _load_mvp_rule_ids(config_path: Path | None = None) -> list[str]:
    path = config_path or MVP_CONFIG_PATH
    with path.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    return [rule_id for key in keys for rule_id in cfg.get(key, [])]


def _read_lifecycle(rule_id: str) -> str:
    meta_path = RULE_DB_DIR / rule_id / "metadata.json"
    if not meta_path.exists():
        return "Draft"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    return str(meta.get("lifecycle_stage", "Draft"))


@lru_cache(maxsize=1)
def load_adopted_mvp_rule_ids(config_path: str | None = None) -> frozenset[str]:
    """Return MVP rule IDs whose lifecycle is ``Adopted``."""
    path = Path(config_path) if config_path else MVP_CONFIG_PATH
    return frozenset(
        rule_id
        for rule_id in _load_mvp_rule_ids(path)
        if _read_lifecycle(rule_id) == "Adopted"
    )


def filter_adopted_weights(weights: dict[str, float], adopted: frozenset[str] | None = None) -> dict[str, float]:
    """Keep only adopted rule weights for domain score aggregation."""
    active = adopted if adopted is not None else load_adopted_mvp_rule_ids()
    return {key: value for key, value in weights.items() if key in active}


def clear_adopted_rules_cache() -> None:
    """Clear cached adopted rule IDs (for tests)."""
    load_adopted_mvp_rule_ids.cache_clear()
