# Skill: convert_to_math_spec

## 목적

Rule Markdown을 수학식, 조건식, Score Formula, JSON 규격으로 변환한다.

## 사용 시점

- 02_math_spec_writer가 Rule Markdown 승인 후
- specs/ 역생성(retrofill) 시

## 입력

- `rules/{category}/{RULE_ID}_*.md`
- `docs/TASS-002_Data_Specification.md` (필드명)
- `docs/TASS-005_Scoring_Framework.md` (점수 범위)

## 출력

- `specs/math/{RULE_ID}.math.md`
- `specs/json/{RULE_ID}.json`

## 실행 절차

### Step 1: specs/math/{RULE_ID}.math.md

```markdown
# Math Spec: {RULE_ID}

## Variables
| Symbol | Type | Source | Description |
|--------|------|--------|-------------|

## Parameters
| Name | Default | Range | Description |
|------|---------|-------|-------------|

## Formulas
(수학식, LaTeX 또는 의사코드)

## Conditions
### PASS
(불리언 조건식)

### WARN
(불리언 조건식)

### FAIL
(불리언 조건식)

## Score Formula
score = f(...)

| Grade | Score Range |
|-------|-------------|

## Confidence Delta
## Risk Delta
```

### Step 2: specs/json/{RULE_ID}.json

```json
{
  "rule_id": "TR-001",
  "version": "1.0.0",
  "category": "TR",
  "type": "atomic",
  "inputs": [],
  "parameters": {},
  "conditions": {
    "pass": [],
    "warn": [],
    "fail": []
  },
  "scoring": {
    "grades": []
  },
  "confidence_delta": {},
  "risk_delta": {},
  "outputs": []
}
```

### Step 3: 검증

- Rule Markdown §8-11과 조건·점수 일치
- 입력 필드명 = TASS-002
- Rule 의미 변경 없음

### Step 4: `generate_python_spec` Skill 실행

## 체크리스트

- [ ] math spec 변수 전부 정의
- [ ] PASS/WARN/FAIL 조건식 완전
- [ ] Score Formula 명시
- [ ] JSON이 math와 동일 의미
- [ ] Rule Markdown 점수표 일치
- [ ] Rule 의미 변경 없음
- [ ] specs/math/, specs/json/ 저장 완료
