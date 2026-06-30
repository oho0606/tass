# Documentation Structure

Canonical documentation map for TASS. Specifications come before implementation.

## Foundation Documents (repo root)

| File | Purpose |
|------|---------|
| `README.md` | Public overview and quick start |
| `PROJECT_SPEC.md` | Canonical AI development specification |
| `AI_CONTEXT.md` | Required onboarding for all AI agents |
| `CHANGELOG.md` | Semantic version history |
| `ROADMAP.md` | Post-v1.0 product direction |

## Core Framework (TASS-001–010)

| ID | Document | Status |
|----|----------|--------|
| TASS-001 | `docs/TASS-001_Ideal_Candidate_Definition.md` | Draft → MVP review |
| TASS-002 | `docs/TASS-002_Data_Specification.md` | Draft → MVP review |
| TASS-003 | `docs/TASS-003_System_Architecture.md` | Draft → MVP review |
| TASS-004 | `docs/TASS-004_Rule_Framework.md` | Draft |
| TASS-005 | `docs/TASS-005_Scoring_Framework.md` | Draft → MVP review |
| TASS-006 | `docs/TASS-006_Gate_Framework.md` | Draft → MVP review |
| TASS-007 | `docs/TASS-007_Confidence_Framework.md` | Draft → MVP review |
| TASS-008 | `docs/TASS-008_Risk_Management_Framework.md` | Draft |
| TASS-009 | `docs/TASS-009_Backtest_Framework.md` | Draft |
| TASS-010 | `docs/TASS-010_Trend_Framework.md` | Draft |

## Rule System (TASS-011–027)

| ID | Document | Status |
|----|----------|--------|
| TASS-011 | `docs/TASS-011_Rule_Taxonomy_Specification.md` | **Standard** |
| TASS-012 | `docs/TASS-012_Rule_Specification_Standard.md` | **Standard** |
| TASS-013 | `docs/TASS-013_Rule_Database_Specification.md` | **Standard** |
| TASS-014–027 | Category & composite catalogs | **Frozen** |

## Implementation & Application (TASS-028–032)

| ID | Document | Status |
|----|----------|--------|
| TASS-028 | `docs/TASS-028_Probability_Engine_v1.0.md` | Frozen |
| TASS-029 | Confidence / Risk Engine docs | Frozen |
| TASS-030 | `docs/TASS-030_Python_Implementation_Specification_v1.0.md` | Active |
| TASS-031 | `docs/TASS-031_Backtest_Engine_v1.0.md` | **Frozen** |
| TASS-032 | `docs/TASS-032_Application_Layer_v1.0.md` | **Frozen** |

## MVP Operational SSOT

| Artifact | Purpose |
|----------|---------|
| `config/mvp_operational_rules.yaml` | Frozen list of 26 production MVP rules |
| `rule_database/rules/{RULE_ID}/` | Per-rule SSOT (spec, metadata, changelog) |
| `scripts/retrofill_mvp_rule_ssot.py` | Generate/update MVP SSOT files |
| `scripts/verify_rule_ssot.py` | 3-way catalog ↔ SSOT ↔ engine check |

## Config & Runtime

| Path | Purpose |
|------|---------|
| `config/settings.yaml` | Engine defaults (`mvp_mode: true`) |
| `config/recommendation_v1.yaml` | Recommendation thresholds (MVP 500-pt scale) |
| `config/gate_pipeline_v1.yaml` | Gate pipeline config |
| `config/universe_*.csv` | KRX universe listings |

## Document Rules

- Specifications come before implementation.
- Documents must not introduce forbidden data sources.
- Documents must distinguish Gate, Score, and Confidence.
- MVP mode (500 pt) and Full mode (1000 pt) must be explicitly documented where scoring applies.
- Behavior-affecting doc changes must be reflected in `CHANGELOG.md`.
