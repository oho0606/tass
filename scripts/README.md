# scripts

TASS 운영 자동화 스크립트 모음입니다.

## 주요 스크립트

| 스크립트 | 역할 |
|----------|------|
| `run_daily_picks.py` | 일일 Top 20 종목 추출 실행 |
| `run_daily_pipeline.py` | 전체 파이프라인 (데이터 → 분석 → 출력) |
| `run_backtest.py` | Rule 백테스트 실행 |
| `cache_market_data.py` | 시장 데이터 캐시 |
| `seed_rule_database.py` | Rule DB 초기화·시딩 |
| `retrofill_mvp_rule_ssot.py` | MVP Rule SSOT 역생성 |
| `verify_rule_ssot.py` | Rule SSOT 3-way 검증 |
| `bootstrap_universe.py` | 유니버스 CSV 생성 |
| `generate_universe.py` | KRX 유니버스 자동 생성 |
| `export_openapi.py` | FastAPI → `frontend/openapi.json` 내보내기 |
| `demo_gate_pipeline.py` | Gate Pipeline 데모 실행 |
| `tune_gate_pipeline.py` | Gate 파라미터 튜닝 |
| `tune_recommendation_thresholds.py` | 추천 임계값 튜닝 |
| `validate_phase6_picks.py` | Phase 6 품질 검증 (MVP 기준) |
| `check_rejected_rule_readoption_readiness.py` | Rejected 룰 재채택 준비 상태 점검 |
| `validate_cache.py` | 캐시 데이터 유효성 검사 |
| `verify_backtest_consistency.py` | 백테스트 결과 일관성 검증 |
| `start_stack.ps1` | 로컬 전체 스택 기동 (PowerShell) |

## 사용 예시

```bash
python scripts/run_daily_picks.py --universe config/universe_sample.csv
python scripts/run_backtest.py --rules TR0001 TR0002
python scripts/cache_market_data.py --universe config/universe_krx_backtest.csv
python scripts/seed_rule_database.py
python scripts/tune_recommendation_thresholds.py --settings config/settings_full.yaml --recommendation-config config/recommendation_full_v1.yaml --verify-only
```
