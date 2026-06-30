# Skill: generate_python_spec

## 목적

Math Spec을 Python 구현 명세로 변환한다. 함수명, 입력, 출력, 예외처리, 복잡도를 정의한다.

## 사용 시점

- `convert_to_math_spec` 완료 후
- 02_math_spec_writer가 Python 구현 핸드오프 전

## 입력

- `specs/math/{RULE_ID}.math.md`
- `specs/json/{RULE_ID}.json`
- `rules/{category}/{RULE_ID}_*.md` §17 Python 인터페이스

## 출력

- `specs/python/{RULE_ID}.python.md`

## 실행 절차

### Step 1: specs/python/{RULE_ID}.python.md 작성

필수 섹션:

```markdown
# Python Spec: {RULE_ID}

## Module
engine.rules.{category}.{module}

## Function
def {function_name}(...) -> RuleResult:

## Input Types
| Parameter | Type | Description |

## Output Type
RuleResult (engine.core.types)

## Algorithm Steps
1. ...
2. ...

## Exceptions
| Condition | Exception | Handling |

## Complexity
Time: O(...)
Space: O(...)

## Dependencies
- engine.core.types
- engine.indicators.*

## Test Scenarios
(rules/ §18 매핑)

## Example
(pseudocode or signature example)
```

### Step 2: RuleResult 필드 매핑

```python
@dataclass
class RuleResult:
    rule_id: str
    status: Literal["PASS", "WARN", "FAIL"]
    score: float
    confidence_delta: float
    risk_delta: float
    reasons: list[str]
    metadata: dict
```

### Step 3: 03_python_implementer 핸드오프

## 체크리스트

- [ ] 함수명이 rules/ §17과 일치
- [ ] 입력 타입 명시 (DataFrame, RuleResult dict 등)
- [ ] RuleResult 반환
- [ ] 예외 조건 정의
- [ ] Time/Space 복잡도 명시
- [ ] 테스트 시나리오 매핑
- [ ] specs/python/ 저장 완료
