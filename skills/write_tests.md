# Skill: write_tests

## 목적

Unit Test, Integration Test, Edge Case, Failure Case, Regression Test를 생성한다.

## 사용 시점

- 03_python_implementer가 Rule/Engine 구현 후
- 백테스트 전 최소 품질 게이트
- 버그 수정 후 회귀 방지

## 입력

- `specs/python/{RULE_ID}.python.md`
- `rules/{category}/{RULE_ID}_*.md` §18 테스트
- `engine/**/*.py` (구현 대상)

## 출력

- `tests/unit/test_{rule_id}.py`
- `tests/integration/test_{pipeline}.py`
- `tests/fixtures/` (synthetic OHLCV)

## 실행 절차

### 1. Unit Test (Rule별)

Rule §18 필수 시나리오 각각 1+ 테스트:

| 시나리오 | 설명 |
|----------|------|
| 정상 상승 | PASS 기대 |
| 횡보 | WARN 또는 낮은 점수 |
| 하락 | FAIL 기대 |
| 급등 후 실패 | WARN/FAIL |
| 거래량 부족 | WARN |

```python
def test_trend_001_uptrend_pass():
    df = make_uptrend_ohlcv(n=60)
    result = evaluate_higher_high(df)
    assert result.status == "PASS"
    assert result.score >= 14
```

### 2. Integration Test

- Data → Indicator → Rule → Domain 파이프라인
- 캐시된 fixture 사용 (네트워크 없음)

### 3. Edge Case

- 빈 DataFrame
- NaN 포함
- 단일 행
- Lookback 미달

### 4. Failure Case

- FAIL 조건 명시적 트리거
- score == 0 확인

### 5. Regression Test

- 고정 fixture + 고정 score 스냅샷
- 구현 변경 시 의도적 diff만 허용

### 6. 실행

```bash
pytest tests/ -v
```

## 체크리스트

- [ ] Rule §18 모든 시나리오 커버
- [ ] Edge case (empty, NaN, short) 포함
- [ ] Integration test 존재
- [ ] Fixture가 synthetic (OHLCV-only)
- [ ] pytest 전체 통과
- [ ] 네트워크 의존 테스트 격리 (@pytest.mark.network)
