#!/usr/bin/env python3
"""Tests for regime baseline validation script."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.validate_regime_baselines import validate_regimes


def test_validate_regimes_structure():
    report = validate_regimes(
        Path("config/universe_sample.csv"),
        top_n=5,
        use_cache=True,
        min_bull_gate_eligible=1,
    )
    assert "current" in report["scenarios"]
    assert "bull" in report["scenarios"]
    assert report["scenarios"]["bull"]["gate_eligible"] >= report["scenarios"]["current"]["gate_eligible"]


def test_regime_validation_output_schema():
    path = Path("output/regime_validation.json")
    if not path.exists():
        return
    report = json.loads(path.read_text(encoding="utf-8"))
    assert "scenarios" in report
    assert "checks" in report
