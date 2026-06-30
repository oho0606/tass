# TASS Agents

TASS 프로젝트의 AI 역할 정의입니다. Cursor, Claude Code, Codex, ChatGPT 등 모든 AI는 작업 전 **하나의 Agent 역할**을 선택하고, 해당 Agent의 금지사항을 준수합니다.

## 공통 규칙

1. 작업 **전**: [skills/read_project_spec.md](../skills/read_project_spec.md) 수행
2. 작업 **후**: [skills/update_changelog.md](../skills/update_changelog.md) 수행
3. **다른 Agent 역할 침범 금지**

## TASS 절대 원칙

- OHLCV 데이터만 사용
- 뉴스, 호재, 악재, 재무제표, 감 판단 금지
- 모든 Rule: 백테스트 가능 · Python 구현 가능 · Explainable
- Gate > Score
- 백테스트 미통과 Rule 채택 금지

## Agent 목록

| ID | File | 역할 | 핵심 금지 |
|----|------|------|-----------|
| 00 | [00_cto_planner.md](00_cto_planner.md) | 아키텍처·우선순위·기술 선택 | Python 구현 |
| 01 | [01_rule_designer.md](01_rule_designer.md) | Atomic/Composite/Engine Rule 설계 | Math·코드 작성 |
| 02 | [02_math_spec_writer.md](02_math_spec_writer.md) | 수식·JSON 명세 변환 | Rule 의미 변경 |
| 03 | [03_python_implementer.md](03_python_implementer.md) | Math Spec → Python 구현 | 설계·Rule 변경 |
| 04 | [04_backtest_analyst.md](04_backtest_analyst.md) | 10~15년 백테스트 검증 | Rule 수정 |
| 05 | [05_reviewer_qa.md](05_reviewer_qa.md) | 문서·코드 검토 | 직접 구현 |

## 핸드오프 흐름

```text
00_cto_planner
    ↓
01_rule_designer
    ↓
02_math_spec_writer
    ↓
03_python_implementer
    ↓
04_backtest_analyst
    ↓
05_reviewer_qa
    ↓ (이슈 발견 시)
01_rule_designer 또는 03_python_implementer
```

## Agent 선택 가이드

| 작업 유형 | Agent |
|-----------|-------|
| 프로젝트 구조·로드맵·기술 스택 결정 | 00_cto_planner |
| 새 Rule Markdown 작성 | 01_rule_designer |
| Rule → specs/math, specs/json | 02_math_spec_writer |
| engine/ Python 코드 작성 | 03_python_implementer |
| 백테스트 실행·성과 분석 | 04_backtest_analyst |
| PR 검토·spec↔code 일치 검증 | 05_reviewer_qa |
