# AI Context

This file is the onboarding context for any AI agent working on TASS.

Before making changes, every AI must read these files in order:

1. `PROJECT_SPEC.md`
2. `AI_CONTEXT.md`
3. `CHANGELOG.md`
4. `README.md`
5. `agents/README.md`

Then execute `skills/read_project_spec.md` and adopt **one Agent role** from `agents/`.

## Project Identity

TASS is an AI-based technical analysis stock recommendation platform.

It is not a charting tool, not a discretionary trading assistant, and not a news-based recommendation system.

The user visits the service to see `Today's Picks`, reviews the TOP 20 recommended stocks, checks the recommendation reasons, and decides whether to buy.

## Agent and Skill System

| Folder | Purpose |
|--------|---------|
| `agents/` | AI role definitions (00–05) |
| `skills/` | Executable procedures (read_project_spec, update_changelog, etc.) |
| `specs/` | Machine-readable Rule specs (math, json, python) |
| `rules/` | Human-readable Rule Markdown (by category: `tr/`, `ma/`, …) |
| `rules/catalog/TR_v1.0.yaml` | Frozen TR rule catalog (80 rules, TASS-014) |
| `rules/catalog/MA_v1.0.yaml` | Frozen MA rule catalog (60 rules, TASS-015) |
| `rules/catalog/Composite_v1.0.yaml` | Frozen Composite Rule Library (130 rules, TASS-027) |
| `rules/registry.yaml` | Official Rule Registry (seed source) |
| `rule_database/` | **Rule Database SSOT** (TASS-013) |
| `docs/` | Framework documents (TASS-001–010) |

**All Agents must:**

1. Run `skills/read_project_spec.md` before work
2. Run `skills/update_changelog.md` after work
3. Never cross into another Agent's role

## Non-Negotiable Principles

- Do not predict the future.
- Select statistically favorable candidates.
- Use only technical analysis data (OHLCV and derived indicators).
- Do not use news, disclosures, earnings, financial statements, politics, SNS, YouTube, communities, analyst opinions, themes, or rumors.
- Gate has priority over total score.
- Every Rule must belong to exactly one taxonomy category (TASS-011).
- Every Rule must be registered in the Rule Database (`rule_database/`) before implementation.
- Every Rule must be measurable, implementable, backtestable, explainable, and versioned.
- Design and specification come before code.
- Rules not passing backtest must not be adopted.

## Current Phase

TASS is in **MVP Implementation + Phase 6 Product Validation** (v1.0-rc1).

| Area | Status |
|------|--------|
| Engine (MVP 3-domain) | Active — `mvp_mode: true` default |
| Rule SSOT (MVP 26 rules) | Complete — `scripts/verify_rule_ssot.py` |
| Universe | 59 liquid KRX names (`config/universe_krx_mvp.csv`) |
| API + Frontend | Active (Today's Picks BFF) |
| Full Engine (1000 pt) | Implemented, not production default (v1.3) |
| Backtest adoption | **17 Adopted / 9 Rejected** (26/26 resolved) |

Allowed work:

- Python engine, API, tests, scripts, frontend
- MVP Rule SSOT maintenance and backtest validation
- Universe bootstrap and cache validation

Deferred:

- Full Engine as production default
- Live trading execution
- Adopting non-MVP rules without backtest

## Architecture Direction

```text
OHLCV
↓
Data Engine
↓
Indicator Engine
↓
Atomic Rules
↓
Composite Rules
↓
Domain Engines
↓
Master Score Engine
↓
Gate Engine
↓
Recommendation Engine
↓
Today's Picks (Top 20)
```

## Recommendation Direction

TASS should reduce a broad stock universe into a small set of high-probability candidates:

```text
2700 stocks
↓
Primary filters
↓
100-300 candidates
↓
Detailed technical analysis
↓
Final score
↓
Gate PASS
↓
TOP 20 Today's Picks
```

## AI Behavior Rules

When working on TASS:

1. Read the foundation documents first (`skills/read_project_spec`).
2. Select one Agent role and follow its prohibitions.
3. Do not change the project structure without explicit user instruction.
4. Do not add implementation before the relevant specification exists.
5. Do not invent Rule logic without a Rule document.
6. Do not mix forbidden data into the system.
7. Preserve consistency between rules, specs, engine, and tests.
8. Update `CHANGELOG.md` for meaningful project changes.

## Next Recommended Work

1. Full Engine threshold re-tune when switching `mvp_mode: false` (v1.3 — deferred).
2. Re-run full grid `tune_recommendation_thresholds.py` when gate_eligible pool exceeds 25.
3. Re-adopt Rejected rules only after spec revision — see `output/rejected_rules_status.json`.
