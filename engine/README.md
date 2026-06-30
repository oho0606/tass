# engine

TASS 핵심 Python 엔진 구현체입니다 (TASS-030 기준).

## 구조

| 디렉토리 | 역할 |
|----------|------|
| `application/` | Application Service (RecommendationService, BacktestService) |
| `backtest/` | Backtest Engine v1.0 |
| `confidence/` | Confidence 산정 엔진 |
| `core/` | Rule Registry, Rule Database, Taxonomy |
| `data/` | 데이터 로더, Yahoo/KIS 어댑터, 캐시 |
| `domains/` | Domain별 점수 엔진 (TR, MA, VL 등) |
| `gate/` | Gate Pipeline (시장 환경·유동성·추세 차단) |
| `indicators/` | 기술적 지표 계산 (MA, RSI, MACD, ATR, OBV 등) |
| `probability/` | 확률 모델 |
| `recommendation/` | 추천 엔진 (Top 20 선별) |
| `risk/` | 리스크 엔진 |
| `rules/` | Rule 구현체 (`ma/`, `tr/`, `vl/` 등) |
| `scoring/` | 종합 스코어링 엔진 (1000점 체계) |

## 진입점

```python
from engine.application.recommendation_service import RecommendationService
```

설계 문서: [docs/TASS-030_Python_Implementation_Specification_v1.0.md](../docs/TASS-030_Python_Implementation_Specification_v1.0.md)
