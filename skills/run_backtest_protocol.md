# Skill: run_backtest_protocol

## 목적

백테스트 절차를 표준화한다. 데이터 검증, 수수료, 슬리피지, 성과 측정, 리포트 생성을 포함한다.

## 사용 시점

- 04_backtest_analyst가 Rule 검증 시
- Rule 채택/거부 결정 전
- MVP 이후 정기 검증

## 입력

- `docs/TASS-009_Backtest_Framework.md`
- 구현된 Rule/Engine (`engine/`)
- KOSPI/KOSDAQ OHLCV (10~15년)
- `config/backtest.yaml` (수수료, 슬리피지)

## 출력

- `backtest/reports/{RULE_ID}_{YYYY-MM-DD}.md`
- 성과 지표 JSON (`backtest/reports/{RULE_ID}_{date}.json`)

## 실행 절차

### 1. 데이터 검증

- [ ] OHLCV 결측률 < 1%
- [ ] 수정주가 반영
- [ ] 거래정지·상장폐지 처리 정책 적용
- [ ] KOSPI + KOSDAQ 유니버스

### 2. 백테스트 설정

| 항목 | 기본값 |
|------|--------|
| 기간 | 최근 10~15년 |
| 빈도 | Daily |
| 수수료 | 0.015% (매매 각) |
| 슬리피지 | 0.1% |
| 초기 자본 | 100,000,000 KRW |

### 3. Rule 신호 생성

- Rule PASS 시 진입 신호
- ATR 기반 손절 (TASS-008)
- 목표가 10~20% (Rule별 정의)

### 4. 성과 측정

필수 지표:

- 승률 (Win Rate)
- 평균수익률 (Avg Return)
- 평균손실 (Avg Loss)
- 손익비 (Reward/Risk)
- Profit Factor
- Sharpe Ratio
- Sortino Ratio
- MDD
- CAGR
- 거래횟수

### 5. 과최적화 검사

- In-sample (70%) vs Out-of-sample (30%) 비교
- 파라미터 ±20% 민감도 테스트
- 거래횟수 < 30이면 "표본 부족" 경고

### 6. 리포트 생성

```markdown
# Backtest Report: {RULE_ID}
Date: {date}
Period: {start} ~ {end}

## Summary
| Metric | Value |
|--------|-------|

## Overfitting Analysis
...

## Recommendation
ADOPT / REJECT / REVISE
```

### 7. 00_cto_planner 또는 01_rule_designer에게 전달

## 체크리스트

- [ ] 데이터 검증 완료
- [ ] 수수료·슬리피지 반영
- [ ] 8개 이상 지표 산출
- [ ] 과최적화 분석 포함
- [ ] 리포트 저장 (backtest/reports/)
- [ ] ADOPT/REJECT/REVISE 권고 명시
- [ ] Rule 직접 수정하지 않음
