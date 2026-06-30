# Skill: write_rule_spec

## 목적

Atomic Rule, Composite Rule, Engine Rule의 Markdown 명세를 표준 템플릿에 따라 작성한다.

## 사용 시점

- 01_rule_designer가 신규 Rule 작성 시
- 기존 Draft Rule 보완 시
- 백테스트 실패 후 Rule 재설계 시

## 입력

- Rule 카테고리 (TR, MA, PA, VL, MO, VO, MS, SR, BO, PB, PT, CS, GP, RK, EN, EX, MR, MT, CF, DQ, MTA)
- Rule 유형 (Atomic / Composite / Engine)
- CTO 우선순위 지시
- [rules/RULE-000_RULE_TEMPLATE.md](../rules/RULE-000_RULE_TEMPLATE.md)

## 출력

- `rules/{category}/{RULE_ID}_{NAME}.md`
- Status: Draft (초기)

## 실행 절차

1. `read_project_spec` 완료 확인

2. Rule ID 할당 ([rules/RULE_STRUCTURE.md](../rules/RULE_STRUCTURE.md) 준수)
   - Atomic: `{CAT}-001`, `{CAT}-002`, ...
   - Composite: `{CAT}-C001`, ...
   - Engine: `{CAT}-E001`, ...

3. RULE-000 템플릿의 모든 섹션 작성

4. Rule 유형별 필수 내용

**Atomic Rule:**
- 단 하나의 Fact만 판단
- 추론·예측 금지
- OHLCV 입력만

**Composite Rule:**
- Atomic Rule 결과만 입력
- 의미(Meaning) 조합

**Engine Rule:**
- Atomic + Composite 실행 순서
- Domain Score 산출 (예: Trend /200)

5. 필수 섹션 확인
   - Purpose, 입력 데이터, PASS/WARN/FAIL
   - 점수 기준 표 (§11)
   - Confidence/Risk 영향 (§12-13)
   - Python 인터페이스 (§17): 함수명, 입력, 출력
   - 테스트 시나리오 (§18)
   - Composite 연결 (§21)

6. `rules/README.md`에 Rule 등록 (필요 시)

7. 02_math_spec_writer에게 핸드오프

## 체크리스트

- [ ] RULE-000 템플릿 준수
- [ ] Rule ID 유일
- [ ] Atomic = Fact 1개
- [ ] OHLCV-only 입력
- [ ] PASS/WARN/FAIL 명확
- [ ] 점수 표 포함
- [ ] Python 함수명 정의
- [ ] 테스트 시나리오 5개 이상
- [ ] Status: Draft 표기
