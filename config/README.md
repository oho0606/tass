# config

TASS 런타임 설정 파일 모음입니다.

## 파일 목록

| 파일 | 역할 |
|------|------|
| `settings.yaml` | 핵심 엔진 설정 (어댑터, top_n, lookback_days 등) |
| `settings_full.yaml` | Full Engine 검증용 설정 (`mvp_mode: false`) |
| `app_settings.py` | Pydantic `AppSettings` (`.env` 바인딩) |
| `gate_pipeline_v1.yaml` | Gate Pipeline 파라미터 |
| `recommendation_v1.yaml` | 추천 엔진 임계값 |
| `recommendation_full_v1.yaml` | Full Engine 임계값 베이스라인 (1000점 스케일) |
| `chart_criteria_v1.yaml` | 조건식용 차트 지표 기준 기간 |
| `confidence_v1.yaml` | Confidence 산정 설정 |
| `backtest_v1.yaml` | Backtest Engine 설정 |
| `probability_v1.yaml` | 확률 모델 설정 |
| `risk_v1.yaml` | 리스크 엔진 설정 |
| `mvp_operational_rules.yaml` | MVP 운영 Rule 26개 목록 |
| `universe_sample.csv` | 샘플 종목 유니버스 |
| `universe_krx_backtest.csv` | KRX 백테스트용 전체 유니버스 |
| `universe_krx_mvp.csv` | MVP 운영용 유니버스 |
| `secrets/` | 민감 키 (`.gitignore` 적용) |

## 주요 설정 (`settings.yaml`)

```yaml
adapter: yahoo          # 데이터 어댑터 (yahoo / kis / kiwoom)
top_n: 20              # Today's Picks 추출 종목 수
min_bars: 60           # 최소 봉 수
lookback_days: 400     # 데이터 조회 기간
cache_dir: data/cache
output_dir: output
```

환경 변수는 `.env` 파일로 관리하며 `app_settings.py`가 로드합니다. `.env.example` 참조.
