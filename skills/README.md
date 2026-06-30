# TASS Skills

TASS 프로젝트의 AI 작업 절차입니다. 모든 Skill은 **독립적으로 실행 가능**하며 Markdown으로 작성되었습니다.

## 공통 규칙

- 모든 Agent는 작업 전 `read_project_spec`, 작업 후 `update_changelog`를 수행합니다.
- Skill은 Agent 역할을 대체하지 않습니다. Skill은 **절차**, Agent는 **책임**입니다.

## Skill 목록

| File | 목적 |
|------|------|
| [read_project_spec.md](read_project_spec.md) | 프로젝트 현재 상태 파악 |
| [write_rule_spec.md](write_rule_spec.md) | Rule Markdown 작성 |
| [convert_to_math_spec.md](convert_to_math_spec.md) | Rule → Math/JSON 명세 |
| [generate_python_spec.md](generate_python_spec.md) | Math Spec → Python 명세 |
| [write_tests.md](write_tests.md) | 테스트 코드 작성 |
| [run_backtest_protocol.md](run_backtest_protocol.md) | 백테스트 절차 실행 |
| [update_changelog.md](update_changelog.md) | CHANGELOG 기록 |

## 실행 순서 (신규 Rule 파이프라인)

```text
read_project_spec
    ↓
write_rule_spec          (01_rule_designer)
    ↓
convert_to_math_spec     (02_math_spec_writer)
    ↓
generate_python_spec     (02_math_spec_writer)
    ↓
[03_python_implementer: engine/ 구현]
    ↓
write_tests
    ↓
run_backtest_protocol    (04_backtest_analyst)
    ↓
update_changelog
```

## Skill 의존 관계

| Skill | 선행 Skill | 후행 Skill |
|-------|-----------|-----------|
| read_project_spec | — | 모든 Skill |
| write_rule_spec | read_project_spec | convert_to_math_spec |
| convert_to_math_spec | write_rule_spec | generate_python_spec |
| generate_python_spec | convert_to_math_spec | (구현) |
| write_tests | (구현) | run_backtest_protocol |
| run_backtest_protocol | write_tests | update_changelog |
| update_changelog | — | — |
