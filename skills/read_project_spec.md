# Skill: read_project_spec

## 목적

작업 시작 전 TASS 프로젝트의 현재 상태를 파악한다. 모든 Agent의 **첫 번째 필수 작업**이다.

## 사용 시점

- 모든 Agent 작업 시작 전
- 긴 작업 중단 후 재개 시
- 다른 Agent 핸드오프 수신 후
- Phase 전환 후 첫 작업

## 입력

없음 (고정 읽기 목록 사용)

## 출력

- 프로젝트 현재 Phase 요약 (mental note 또는 작업 로그)
- 관련 Rule/Engine 상태 파악
- 이번 작업 범위 결정에 필요한 컨텍스트

## 실행 절차

1. 아래 파일을 **순서대로** 읽는다.

```text
1. PROJECT_SPEC.md
2. AI_CONTEXT.md
3. CHANGELOG.md
4. README.md
5. agents/README.md
```

2. 작업과 관련된 추가 문서를 읽는다.

| 작업 유형 | 추가 읽기 |
|-----------|-----------|
| Rule 설계 | docs/TASS-011 … TASS-015, rules/catalog/, rules/RULE-000, rules/registry.yaml, rule_database/ |
| Math Spec | rules/{대상 Rule}, docs/TASS-002, docs/TASS-005 |
| Python 구현 | specs/python/, specs/json/, engine/core/, docs/TASS-003 |
| 백테스트 | docs/TASS-009, backtest/README.md |
| 아키텍처 | docs/TASS-003, docs/DEVELOPMENT_ROADMAP.md |

3. 현재 Phase 확인 (`AI_CONTEXT.md` §Current Phase)

4. 금지 데이터 목록 확인 (뉴스, 재무제표, SNS 등)

5. 작업 범위가 명확하지 않으면 00_cto_planner에게 에스컬레이션

## 체크리스트

- [ ] PROJECT_SPEC.md 읽음
- [ ] AI_CONTEXT.md 읽음
- [ ] CHANGELOG.md 최신 버전 확인
- [ ] README.md 읽음
- [ ] agents/README.md 읽음
- [ ] 현재 Phase 파악
- [ ] 금지 데이터 목록 인지
- [ ] 작업 범위 명확
