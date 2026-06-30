# tests

TASS 자동화 테스트 스위트입니다.

## 구조

| 디렉토리 | 역할 |
|----------|------|
| `unit/` | 단위 테스트 (~30개 파일) |
| `integration/` | 통합 테스트 (파이프라인 전체 흐름) |
| `regression/` | 회귀 테스트 (baseline JSON 비교) |
| `fixtures/` | 공통 테스트 픽스처 (OHLCV, 시장 캐시 등) |

## 단위 테스트 커버리지

- Rule 계산 (TR, MA, VL, Composite)
- Gate Pipeline, Market Context
- Scoring Engine, Confidence Engine
- Probability Engine, Risk Engine
- Domain Engines (추세·이동평균·거래량)
- Rule Database, Taxonomy
- 데이터 파이프라인, 지표 계산
- Application Services (추천, 백테스트)
- API 계약 (`tests/api/`)

## 회귀 테스트

`regression/baselines/` — TR0001 기준 시장 국면별(bull/bear/sideways/gap_up/high_volume) JSON baseline.

## 실행

```bash
pytest tests/ -q
pytest tests/unit/ -q
pytest tests/integration/ -q
pytest tests/regression/ -q
```
