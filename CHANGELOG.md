# Changelog

All notable changes to TASS will be documented in this file.

TASS follows Semantic Versioning.

## [Unreleased]

## [v1.0.0] - 2026-06-30

### Added

- `config/chart_criteria_v1.yaml` — 조건식 차트 지표 기준(기간) 설정 파일.
- `engine/indicators/config.py` — 지표 기준 로더(`IndicatorCriteria`) 추가.
- `config/settings_full.yaml` — Full Engine 검증용 파이프라인 설정 (`mvp_mode: false`).
- `config/recommendation_full_v1.yaml` — Full Engine(1000점 스케일) 임계값 베이스라인.
- `scripts/check_rejected_rule_readoption_readiness.py` — Rejected 9개 룰의 재채택 준비 상태 리포트 생성.
- `api` picks history endpoint (`/picks/history`) 및 히스토리 응답 스키마.
- `frontend/src/components/analyze/history-panel.tsx` — 최근 추천 이력 패널.

### Changed

- `engine/indicators/registry.py` — 기준 설정 기반 커스텀 지표 컬럼 계산 지원(기존 기본 컬럼 호환 유지).
- `tests/unit/test_indicators.py` — 차트 기준 설정 주입 테스트 추가.
- `scripts/bootstrap_universe.py` — `--require-live` 옵션으로 라이브 유니버스 수집 실패 감지 가능.
- `scripts/tune_recommendation_thresholds.py` — `--settings`, `--recommendation-config` 지원 및 Full-mode grid/헬스 체크 로직 추가.
- `config/README.md`, `scripts/README.md` — Full-mode 설정/튜닝 사용 예시 반영.
- `output/rejected_rules_readiness.json` 생성 경로 반영 (재채택 준비 상태 자동 점검).
- `frontend/e2e/dashboard.spec.ts` — 분석 모드 컨트롤 가시성 E2E 케이스 추가.
- `frontend` API client/hooks — picks history 조회(`api.picksHistory`, `usePicksHistory`) 추가.
- `tests/api/test_api.py` — `/picks/history` 응답 테스트 추가.
- `.github/workflows/ci.yml`, `.github/workflows/daily-picks.yml` — Full-mode recommendation threshold verify step 추가.
- `ROADMAP.md`, `README.md` — 알림/포트폴리오 비중 축소 및 단일 사용자 온디맨드 조회형 방향 명시.

## [v1.0.0-rc7] - 2026-06-30

### Added

- `scripts/validate_regime_baselines.py` — current vs bull (UP/UP) regime pipeline comparison.
- `output/rejected_rules_status.json` — Rejected 9 rules manifest and re-adoption path.
- `tune_recommendation_thresholds.py --regime`, `--verify-only`, gate-eligible filter.

### Changed

- Recommendation tuning uses **gate-eligible inputs only** (matches production rank_top20).
- CI/daily-picks: regime validation + recommendation verify-only checks.
- `recommendation_v1.yaml` — re-validated 2026-06-30; **no threshold change** (gate is bottleneck).

### Regime Validation (2026-06-30)

| Regime | gate_eligible | picks | rec_pool |
|--------|---------------|-------|----------|
| current (KOSDAQ CRASH) | 17 | 16 | 16 |
| bull (UP/UP) | 20 | 19 | 19 |

Recommendation gates are not the bottleneck; gate pipeline is.

## [v1.0.0-rc6] - 2026-06-30

### Added

- `engine/core/adopted_rules.py` — load Adopted MVP rules from rule_database lifecycle.
- `engine/core/mvp_adoption.py` — finalize non-Adopted rules to Rejected (TASS-009).
- `scripts/finalize_mvp_rule_adoption.py` — REVISE/Implemented → Rejected workflow.
- `scripts/verify_adopted_scoring.py` — cross-check domain engines use Adopted rules only.
- Phase 6 check: `mvp_rules_resolved` (26/26 Adopted or Rejected).

### Changed

- Domain engines (`trend`, `moving_average`, `volume`) — score only **Adopted** rules at runtime.
- REVISE 9 rules finalized → **Rejected** (TR0003, CTR004/006/008, MA0002/003/012/021/029).
- `config/recommendation_v1.yaml`, `mvp_operational_rules.yaml` — validation composites exclude Rejected CTR rules.
- `adopt_mvp_rules.py` — auto-finalize after backtest run.
- CI: `verify_adopted_scoring.py` in api-smoke and daily-picks workflows.

### Phase 6 Accuracy (2026-06-30)

- **17 Adopted / 9 Rejected / 0 Implemented limbo** — all 26 MVP rules resolved.
- Picks regenerated with adopted-only scoring; Phase 6 **PASSED**.

## [v1.0.0-rc5] - 2026-06-30

### Added

- **Gate FAIL UX** — pipeline `FAIL` 종목은 Today's Picks TOP 20에서 제외, `gate_blocked` 관찰 목록(최대 5)으로 분리.
- `RankTop20Result`, `is_gate_eligible()` — gate-eligible picks vs blocked candidates.
- Frontend `Gate 차단 관찰 목록` 섹션 (analyze flow SSE + UI).
- Phase 6 check: `picks_gate_eligible` (TOP picks에 gate FAIL 없음).
- CI: `validate_phase6_picks.py` in `ci.yml` (api-smoke) and `daily-picks.yml`.

### Phase 6 Adoption (2026-06-30)

- `adopt_mvp_rules.py --max-symbols 30`: **17 Adopted**, 0 Rejected (26 rules, 30 symbols).

### Changed

- `engine/recommendation/top20.py` — `rank_top20()` returns `RankTop20Result`; `eligible_only=False` for full ranking API.
- `DailyPicksResult`, API `DailyPicksResponse`, picks JSON — optional `gate_blocked` field.

## [v1.0.0-rc4] - 2026-06-30

### Added

- `scripts/tune_gate_pipeline.py` — dry-run sweep for `gate_pipeline_v1.yaml` (combine_mode, crash_drawdown, trend floor).
- Market Gate `combine_mode: listing` — evaluate KOSPI/KOSDAQ index by symbol listing market (KS/KQ).

### Changed

- `config/gate_pipeline_v1.yaml` — `combine_mode: listing` (fixes KOSPI picks blocked when only KOSDAQ is CRASH).
- `config/settings.yaml` — `trend_floor_score` 100 → 80 (MVP gate tuning sweep).
- `engine/gate/market_gate.py`, `market_context.py`, `evaluate.py`, `report.py` — listing-aware effective market trend.
- Phase 6 picks regenerated: **14/20 pipeline gate PASS** (was 0/20).

### Phase 6 Gate Tuning (2026-06-30)

- Root cause: KOSDAQ index CRASH (17.6% drawdown) with `worst` combine mode blocked all symbols.
- Fix: listing-aware Market Gate + trend floor 80 → `validate_phase6_picks.py` **PASSED**.

## [v1.0.0-rc3] - 2026-06-20

### Added

- `scripts/adopt_mvp_rules.py` — universe backtest → lifecycle Adopted/Rejected per TASS-009.
- `scripts/validate_phase6_picks.py` — Phase 6 validation (picks, cache, SSOT, adoption).
- `RuleDatabase.upsert_from_folder()` — sync folder metadata into SQLite SSOT.
- `engine/backtest/registry.py` — CTR composite DataFrame wrapper for walk-forward backtest.

### Changed

- `engine/core/rule_database.py` — `set_lifecycle_stage()` auto-upserts from folder on FK miss.
- `scripts/validate_phase6_picks.py` — recommendation assignments vs pipeline gate (informational).
- Daily picks generated on 59-name universe (`output/picks_2026-06-20.json`).

### Phase 6 Results (2026-06-20)

- Cache: 61 parquet files (≥60 bars each).
- Picks: TOP 20 from 59 candidates, all explainable.
- MVP adoption: **15 Adopted**, 1 Rejected (8-symbol sample, incl. CTR composites).
- `validate_phase6_picks.py`: **PASSED**.

## [v1.0.0-rc2] - 2026-06-20

### Added

- **MVP Rule SSOT** — `config/mvp_operational_rules.yaml` (26 production rules).
- `scripts/retrofill_mvp_rule_ssot.py` — generate specification/README/changelog per MVP rule.
- `scripts/verify_rule_ssot.py` — 3-way catalog ↔ SSOT ↔ engine verification.
- `scripts/bootstrap_universe.py` — PyKRX fetch with static MVP fallback.
- `config/universe_krx_mvp.csv` — 59 liquid KRX names (39 KOSPI + 20 KOSDAQ).
- `tests/unit/test_mvp_rule_ssot.py` — SSOT completeness + verify script tests.
- `RuleDatabase.set_lifecycle_stage()` — lifecycle transitions with history.

### Changed

- Universe expanded: `universe_krx_backtest.csv` 10 → 59, `universe_sample.csv` 10 → 20.
- `PROJECT_SPEC.md`, `AI_CONTEXT.md`, `DOCUMENTATION_STRUCTURE.md`, `DEVELOPMENT_ROADMAP.md` — phase sync (MVP + Phase 6).
- `docs/TASS-002`, `TASS-003`, `TASS-005`–`TASS-007` — MVP Implementation Notes (v1.0-rc1).
- `rule_database/rules/{MVP_RULE}/` — 26 rules now have full SSOT files (was TR0001 only).

## [v1.0.0-rc1] - 2026-06-19

### Added (Phase 6 — Release Preparation)

- **Recommendation threshold tuning** — MVP-calibrated `config/recommendation_v1.yaml` (gates + grades).
- `scripts/tune_recommendation_thresholds.py` — dry-run threshold sweep.
- `scripts/validate_cache.py` — Data Quality Gate for OHLCV cache.
- `scripts/run_daily_pipeline.py` — cache update → picks → webhook notification.
- `scripts/verify_backtest_consistency.py` — picks vs backtest rule cross-check.
- **Docker Compose** — `docker-compose.yml` (backend, frontend, Redis, PostgreSQL).
- `frontend/Dockerfile` — Next.js standalone production image.
- `.github/workflows/daily-picks.yml` — scheduled daily pipeline (16:00 KST weekdays).
- **Alembic** — initial `daily_picks` table migration scaffold.
- `.env.prod.example` — production environment template.
- `ROADMAP.md` — post-v1.0 product plan.
- Multi-regime regression baselines (`tests/regression/test_regime_baselines.py`).
- OHLCV fixtures: `make_gap_up_ohlcv`, `make_high_volume_ohlcv`.

### Changed

- `config/settings.yaml` — `trend_floor_score` 120 → 100.
- `config/app_settings.py` — `CORS_ORIGINS` from environment.
- `api/app.py` — CORS origins configurable via env.
- `.github/workflows/ci.yml` — frontend build, API smoke, Docker build, regression, E2E jobs.
- `frontend/next.config.ts` — `output: "standalone"` for Docker.
- `frontend/package.json` — `@playwright/test` + `test:e2e` script.
- `pyproject.toml` — Alembic in `[data]` extras.
- `engine/data/validator.py` — `sanitize_ohlcv()` for split-adjusted Yahoo OHLC fixes.
- `scripts/validate_cache.py` — `--repair` flag to rewrite sanitized cache files.
- `scripts/verify_docker_compose.py` — static + CLI compose validation.

## [v0.5.1] - 2026-06-19

### Added

- **Real-data backtest pipeline** — KOSPI/KOSDAQ universe CSV + cached OHLCV loading.
- `engine/application/market_data_loader.py` — cache-first universe OHLCV loader.
- `BacktestService.run_universe_backtest()` / `load_market_data()` — KRX backtest entry points.
- `scripts/cache_market_data.py` — prefetch Yahoo OHLCV into `data/cache`.
- Universe files: `config/universe_kospi_backtest.csv`, `universe_kosdaq_backtest.csv`, `universe_krx_backtest.csv`.
- `tests/integration/test_real_data_backtest.py`, `tests/unit/test_market_data_loader.py`.
- Backtest registry delegates to `catalog_registry` for all atomic rules.

### Changed

- `scripts/run_backtest.py` — `--universe`, `--lookback-days`, `--no-cache`, `--no-fetch`, `--synthetic`.
- `config/backtest_v1.yaml` — `data` section (10-year lookback, default universe).
- `main.py` — backtest subcommand forwards real-data flags.

## [v0.5.0] - 2026-06-19

### Added

- **16 generic domain engines** — price_action, momentum, volatility, market_structure, support_resistance, breakout, pullback, pattern, candlestick, gap, risk, entry, market_regime, multi_timeframe, confirmation, data_quality.
- `engine/domains/_config.py`, `_generic_engine.py`, `bundle.py` — catalog-driven domain evaluation with curated atomic subsets.
- `DomainEngineResult`, `DomainBundle` types; `compute_master_score(bundle=...)` for full 1000-point scoring.
- `tests/unit/test_domain_engines.py` — generic domain + full-mode scoring tests.

### Changed

- `engine/application/recommendation_service.py` — full pipeline uses `evaluate_domain_bundle` when `mvp_mode=False`.
- `engine/scoring/scoring_engine.py` — aggregates generic domain results from bundle.
- MVP mode unchanged: Trend + MA + Volume only (max 500).

## [v0.4.1] - 2026-06-19

### Added

- **TR full catalog** — TR0001–TR0080 (80 rules); TR0001–TR0004 hand-crafted, TR0005+ spec-driven.
- `engine/rules/tr/_name_parser.py`, `_runtime.py`, `registry.py` — TR catalog runtime and registry.
- `scripts/_gen_tr_catalog_rules.py` — TR catalog generator.
- **Composite full catalog** — 130 composite rules (CTR001–CTR010 hand-crafted + 120 ratio-based).
- `engine/rules/composite/_ratio.py` — category ratio aggregation for CMA–CDQ composites.
- `scripts/_gen_composite_rules.py` — composite catalog generator.
- `tests/unit/test_tr_composite_catalog.py` — TR + composite registry smoke tests.

### Changed

- `engine/rules/catalog_registry.py` — TR category registered (**1,160** atomic evaluators).
- `engine/rules/composite/registry.py` — all 130 composite evaluators registered.
- `tests/unit/test_catalog_rules.py`, `test_composite_rules.py` — updated counts.

## [v0.4.0] - 2026-06-19

### Added

- **Catalog rule framework** — `engine/rules/_common/` spec-driven runtime (`RuleSpec`, `SpecRule`, pattern parsers).
- **16 new rule categories** (960 rules): PA, MO, VO, MS, SR, BO, PB, PT, CS, GP, RK, EN, MR, MT, CF, DQ.
- `engine/rules/catalog_registry.py` — master registry (**1,080** atomic evaluators incl. MA + VL).
- `scripts/_gen_all_catalog_rules.py` — YAML/markdown catalog → One Class · One File generator.
- Extended indicators: Stochastic, CCI, MFI, ROC, ADX, Bollinger Bands, true range, historical volatility.
- `tests/unit/test_catalog_rules.py` — registry size + smoke evaluation tests.

### Changed

- `engine/indicators/registry.py` — full indicator set for MO/VO/RK/MR/MT rule evaluation.
- Atomic rules now cover all frozen TASS-011 taxonomy catalogs (except TR partial + Composite).

## [v0.3.6] - 2026-06-19

### Added

- `engine/rules/vl/` — VL0001–VL0060 Volume atomic rules (60 rules).
- `engine/rules/vl/_absolute.py`, `_relative.py`, `_trend.py`, `_spike.py`, `_confirmation.py`, `_quality.py`.
- `engine/domains/volume_engine.py` — Volume Domain Engine (budget 150, 6-rule MVP subset).
- `engine/core/types.py` — `VolumeEngineResult`.
- `scripts/_gen_vl_rules.py`, `_gen_vl_registry.py`.
- `tests/unit/test_vl_rules.py`, `test_volume_engine.py`.

### Changed

- `engine/indicators/` — `relative_volume`, `volume_high_20`, `volume_low_20`, `money_flow` columns.
- `engine/scoring/` — MVP includes `volume` domain (max 500 = Trend 200 + MA 150 + Volume 150).
- `engine/application/recommendation_service.py` — pipeline calls Volume Engine.
- `engine/rules/vl/registry.py` — domain engine subset: VL0001, VL0004, VL0021, VL0041, VL0027, VL0059.
- `docs/TASS-017`, `docs/TASS-030` — VL implementation status.

## [v0.3.5] - 2026-06-19

### Added

- `engine/rules/ma/` — MA0041–MA0060 Slope, Distance & Structure rules (20 rules).
- `engine/rules/ma/_slope.py`, `_structure.py` — shared rule bases.
- `scripts/_gen_ma_rules_batch3.py` — rule generator for MA0041–MA0060.

### Changed

- `engine/rules/ma/registry.py` — **60** MA evaluators (full MA catalog implemented).
- `docs/TASS-015`, `docs/TASS-030`, `rules/ma/README.md` — MA0041–MA0060 status.
- `tests/unit/test_ma_rules.py` — slope/structure tests; registry count 60.

## [v0.3.4] - 2026-06-19

### Added

- `engine/rules/ma/` — MA0022–MA0040 Alignment & Crossover rules (19 rules).
- `engine/rules/ma/_alignment.py`, `_crossover.py` — shared rule bases.
- `scripts/_gen_ma_rules_batch2.py`, `_gen_ma_registry.py` — rule/registry generators.

### Changed

- `engine/rules/ma/registry.py` — 40 MA evaluators; domain engine subset uses structural/alignment rules (MA0029 added; MA0031/MA0033 excluded — latest-bar crossover events dilute daily domain score).
- `engine/domains/moving_average_engine.py` — 6-rule domain evaluation subset.
- `engine/risk/mapping.py` — contiguous upper-bound mapping fixes gap scores (e.g. 20.11) misclassified as Extreme Risk.
- `docs/TASS-015` — MA0022–MA0040 implementation status.
- `tests/unit/test_ma_rules.py` — alignment/crossover tests.

### Fixed

- Integration pipeline picks restored after MA domain subset scoring regression (probability gate no longer fails at ~58%).

## [v0.3.3] - 2026-06-19

### Added

- `engine/rules/ma/` — MA0001–MA0020 Price Position rules (One Class · One File) + MA0021 SMA Bullish Alignment.
- `engine/rules/ma/_helpers.py`, `_scoring.py`, `registry.py` — shared MA rule infrastructure.
- `engine/domains/moving_average_engine.py` — Moving Average Domain Engine (budget 150).
- `engine/core/types.py` — `MovingAverageEngineResult`.
- `tests/unit/test_ma_rules.py`, `test_moving_average_engine.py` — MA rule and domain engine tests.
- `scripts/_gen_ma_rules.py` — MA price-position rule file generator.

### Changed

- `engine/indicators/ma.py` — `compute_ema()`; registry adds `ema_*` columns.
- `engine/scoring/` — MVP includes `moving_average` domain (350 pt max = Trend 200 + MA 150).
- `engine/application/recommendation_service.py` — pipeline calls Moving Average Engine.
- `engine/backtest/registry.py` — MA0002 backtest evaluator.
- `docs/TASS-015` — MA0001–MA0021 implementation status.

## [v0.3.2] - 2026-06-19

### Added

- `engine/application/` — Application Layer v1.0 (Frozen): `RecommendationService`, `BacktestService`.
- `engine/application/settings.py` — `PipelineSettings` from `config/settings.yaml`.
- `engine/application/serializers.py` — JSON/CLI serialization (I/O only).
- `engine/application/types.py` — `DailyPicksResult`, `BacktestServiceResult`.
- `docs/TASS-032_Application_Layer_v1.0.md` — frozen Application Layer specification.
- `tests/unit/test_application_services.py` — recommendation/backtest service unit tests.
- `tests/integration/test_application_pipeline.py` — offline daily picks through Application Service.

### Changed

- `scripts/run_daily_picks.py` — delegates to `RecommendationService` (business logic removed from CLI).
- `scripts/run_backtest.py` — delegates to `BacktestService`.
- `engine/backtest/backtest_engine.py` — `run_and_save()` returns Markdown paths tuple.
- `docs/TASS-030` — Application Layer ✅ v1.0 반영.

## [v0.3.1] - 2026-06-19

### Added

- `engine/backtest/` — Backtest Engine v1.0 (Frozen): walk-forward Rule validation, trade simulation, TASS-009 metrics.
- `config/backtest_v1.yaml` — commission, slippage, hold/stop/take-profit, evaluation thresholds.
- `docs/TASS-031_Backtest_Engine_v1.0.md` — frozen Backtest Engine specification.
- `scripts/run_backtest.py` — offline Rule backtest CLI (synthetic OHLCV).
- `tests/unit/test_backtest_engine.py` — metrics, simulator, rule backtest, engine tests.
- `tests/integration/test_backtest_pipeline.py` — end-to-end backtest pipeline.
- `tests/regression/test_tr_rules_regression.py` — TR0001 baseline regression + reproducibility.

### Changed

- `main.py` — `tass backtest` subcommand 추가 (API는 마지막 단계).
- `docs/TASS-030` — Backtest 구현 상태 ✅ v1.0 반영.
- `backtest/README.md` — Engine·CLI·Regression 안내.

## [v0.3.0] - 2026-06-19

### Added

- `docs/TASS-030_Python_Implementation_Specification_v1.0.md` — frozen Python 구현 표준 (`engine/` 매핑).
- `main.py` — `tass picks` / `tass api` CLI 진입점.
- `engine/core/exceptions.py` — TASS custom exception hierarchy.
- `engine/core/logging.py` — Loguru 기반 구조화 로깅.
- `config/app_settings.py` — `.env` Pydantic Settings.
- `engine/backtest/` — BacktestEngine 스텁 (TASS-009 연동 예정).
- `engine/application/` — RecommendationService 스텁.
- `api/` — FastAPI health/picks placeholder (`pip install -e '.[api]'`).
- `.pre-commit-config.yaml`, `.github/workflows/ci.yml` — Black, Ruff, isort, mypy, pytest CI.
- `tests/unit/test_core_infrastructure.py` — exceptions, settings, backtest 스텁 테스트.
- `tests/regression/`, `logs/`, `database/` — 표준 디렉터리.
- `.env.example`, `requirements.txt`.

### Changed

- `pyproject.toml` — v0.3.0, loguru, dev/api/data/analysis optional groups, Black/Ruff/isort/mypy 설정.
- `README.md` — TASS-030 구조·실행 방법·코드 품질 안내.
- `.gitignore` — logs, .env, coverage 캐시 추가.
- `engine/` — Ruff auto-fix 및 Black 포맷 적용 (2-space → 4-space).

## [v0.2.9] - 2026-06-19

### Added

- `engine/confidence/` — Confidence Engine v1.0 (Frozen): 13-component reliability scoring (0–100).
- `config/confidence_v1.yaml` — component weights and neutral baselines for pending domains.
- `docs/TASS-029_Confidence_Engine_v1.0.md` — frozen Confidence Engine specification.
- `tests/unit/test_confidence_engine.py` — confidence engine unit tests (grades, components, determinism).

### Changed

- `engine/core/types.py` — `ConfidenceResult`, `AgreementReport`, `ConsistencyReport`, `ConfidenceBreakdown`; pick confidence grade/level fields.
- `engine/recommendation/top20.py` — uses master-level Confidence Engine instead of `trend_confidence`.
- `scripts/run_daily_picks.py` — JSON output includes confidence grade/level/stars.

## [v0.2.8] - 2026-06-19

### Added

- `engine/scoring/` — Scoring Engine v1.0 (Frozen): domain budgets, master grades (SSS–F), explainability breakdown.
- `specs/json/SCORING-001.json` — machine-readable scoring spec (20 domain weights, grade thresholds).
- `tests/unit/test_scoring_engine.py` — scoring engine unit tests (budgets, grades, aggregation, determinism).

### Changed

- `engine/gate/basic_gate.py` — `compute_master_score` moved to Scoring Engine; gate module re-exports for compatibility.
- `engine/core/types.py` — `EngineBreakdown`, master `grade` / `interpretation` / `engine_breakdown` on `MasterScoreResult`.
- `engine/recommendation/top20.py` — consumes `MasterScoreResult` domain map and master grade.

## [v0.2.7] - 2026-06-19

### Added

- `engine/core/composite_base.py` — TASS-027 composite rule interface (PASS/PARTIAL/FAIL/UNKNOWN, no scoring).
- `engine/rules/composite/` — composite runner and CTR001–CTR010 Trend Composite implementations.
- [tests/unit/test_composite_rules.py](tests/unit/test_composite_rules.py) — composite rule unit tests.

### Changed

- `engine/domains/trend_engine.py` — uses TASS-027 CTR001–CTR010 as Domain Engine input; verdict-to-score mapping in engine layer only.
- Legacy `engine/rules/tr/composite.py` (TRC001–TRC004) retained but no longer wired to Trend Engine.

## [v0.2.6] - 2026-06-19

### Added

- [docs/TASS-027_Composite_Rule_Library_v1.0.md](docs/TASS-027_Composite_Rule_Library_v1.0.md) — Frozen Composite Rule Library (130 rules, 20 categories).
- [rules/catalog/Composite_v1.0.yaml](rules/catalog/Composite_v1.0.yaml) — machine-readable composite library (CTR001–CDQ002).

### Changed

- `engine/core/taxonomy.py` — support TASS-027 composite library IDs (`CTR001`, `CMA001`, …).
- `engine/core/rule_database.py` — seed composite library from `Composite_v1.0.yaml`.
- `engine/core/types.py` — add `PARTIAL` to `RuleVerdict` for composite state evaluation.
- [rules/catalog/README.md](rules/catalog/README.md) — document all atomic catalogs and composite library.

## [v0.2.5] - 2026-06-18

### Added

- [docs/TASS-015_MA_Rule_Catalog_v1.0.md](docs/TASS-015_MA_Rule_Catalog_v1.0.md) — Frozen MA catalog (60 rules).
- [rules/catalog/MA_v1.0.yaml](rules/catalog/MA_v1.0.yaml) — machine-readable MA catalog.

### Changed

- `engine/core/rule_database.py` — generalized catalog seeding (`*_v*.yaml` in `rules/catalog/`).
- MA subcategories aligned to catalog in [registry.yaml](rules/registry.yaml) and [TASS-011](docs/TASS-011_Rule_Taxonomy_Specification.md).
- Rule Database now seeds **145 rules** (85 TR + 60 MA).

## [v0.2.4] - 2026-06-18

### Added

- [docs/TASS-014_TR_Rule_Catalog_v1.0.md](docs/TASS-014_TR_Rule_Catalog_v1.0.md) — Frozen TR catalog (80 rules).
- [rules/catalog/TR_v1.0.yaml](rules/catalog/TR_v1.0.yaml) — machine-readable catalog.
- [rules/catalog/README.md](rules/catalog/README.md).

### Changed

- TR subcategories aligned to catalog: Direction, Strength, Quality, Slope, Persistence, Exhaustion, Confirmation, State.
- `engine/core/rule_database.py` — seeds TR0005–TR0080 from catalog (status: Frozen).
- TR0002–TR0004 names aligned to catalog (Higher Low, Lower High, Lower Low).
- [rules/tr/README.md](rules/tr/README.md), [TASS-011](docs/TASS-011_Rule_Taxonomy_Specification.md).

## [v0.2.3] - 2026-06-18

### Added

- [docs/TASS-013_Rule_Database_Specification.md](docs/TASS-013_Rule_Database_Specification.md) — Rule Database SSOT.
- [rule_database/](rule_database/) — SQLite schema, per-rule folders, `tass_rules.db`.
- `engine/core/rule_database.py` — `RuleDatabase` API (get, search, validate, history).
- [scripts/seed_rule_database.py](scripts/seed_rule_database.py) — seed from `registry.yaml`.
- [rule_database/rules/TR0001/](rule_database/rules/TR0001/) — reference rule folder (metadata, parameters).
- `tests/unit/test_rule_database.py`.

### Changed

- `engine/core/rule_registry.py` — facade over Rule Database (SSOT).
- [database/README.md](database/README.md) — Rule DB documentation.

## [v0.2.2] - 2026-06-18

### Added

- [docs/TASS-012_Rule_Specification_Standard.md](docs/TASS-012_Rule_Specification_Standard.md) — mandatory 18-section Rule spec.
- [rules/RULE-000_RULE_TEMPLATE.md](rules/RULE-000_RULE_TEMPLATE.md) v2.0.0 aligned with TASS-012.
- `engine/core/rule_base.py` — `BaseRule` with `initialize`, `validate_input`, `calculate`, `evaluate`, `result`, `metadata`.
- `engine/rules/tr/tr0001_higher_high.py` — reference class implementation (`TR0001HigherHighRule`).
- `specs/json/TR0001.json` — full TASS-012 §18 JSON fields.
- `RuleResult.verdict`: PASS | FAIL | UNKNOWN (precondition failure → UNKNOWN).

### Changed

- Canonical Rule IDs: `TR0001`, `TRC001`, `TRE001` (hyphen and TREND-* remain as legacy aliases).
- [rules/registry.yaml](rules/registry.yaml) updated with priority, weight, dependencies, class paths.

## [v0.2.1] - 2026-06-18

### Added

- Official Rule Taxonomy Specification ([docs/TASS-011_Rule_Taxonomy_Specification.md](docs/TASS-011_Rule_Taxonomy_Specification.md)) with 21 category codes.
- [rules/registry.yaml](rules/registry.yaml) — Rule Registry for all categories and registered TR rules.
- `engine/core/taxonomy.py` — CategoryCode enum, rule ID parsing, legacy aliases.
- `engine/core/rule_registry.py` — Registry loader and validation.
- `rules/tr/` — TR category rules (canonical path).
- Unit tests for taxonomy and registry (`tests/unit/test_taxonomy.py`).

### Changed

- Rule IDs migrated: `TREND-*` → `TR-*` (Trend category code TR).
- [rules/RULE_STRUCTURE.md](rules/RULE_STRUCTURE.md) and [RULE-000](rules/RULE-000_RULE_TEMPLATE.md) aligned with TASS-011.
- Engine imports: `engine.rules.tr` (was `engine.rules.trend`).
- Specs renamed: `specs/json/TR-*.json`, etc.

### Deprecated

- `rules/trend/` directory and `TREND-*` Rule ID prefix (aliases preserved in registry).

## [v0.2.0] - 2026-06-18

### Added

- AI Agent system (`agents/00`–`05`) with role boundaries and handoff flow.
- AI Skill system (`skills/`) with 7 executable procedures.
- `specs/` directory for math, JSON, and Python Rule specifications.
- MIT `LICENSE`.
- MVP Python engine: Data, Indicator, Trend Rules, Domain, Gate, Score, Recommendation.
- `scripts/run_daily_picks.py` CLI for Top 20 output.
- Unit and integration tests with synthetic fixtures.

### Changed

- `AI_CONTEXT.md`: Phase updated to MVP Implementation; Agent/Skill references added.
- `README.md`: Project structure, AI workflow, and run instructions added.

## [v0.1.0] - 2026-06-18

### Added

- Established TASS AI Development Specification v1.0.
- Defined TASS as an AI-based technical analysis stock recommendation platform.
- Added Project Foundation structure.
- Added initial documentation, rule, and roadmap foundation files.
- Added AI collaboration context for future AI agents.
