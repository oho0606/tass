# TASS Specs

Rule의 **기계 가독 명세** 계층입니다. 사람이 읽는 Rule은 [rules/](../rules/), 프레임워크는 [docs/](../docs/)에 있습니다.

## 4-Part Rule Specification

| Part | Location | Audience |
|------|----------|----------|
| ① Markdown | `rules/{category}/` | 사람 + AI |
| ② Math | `specs/math/` | AI + 검증 |
| ③ JSON | `specs/json/` | AI + 런타임 |
| ④ Python | `specs/python/` + `engine/` | 구현 |

## Directory layout

```text
specs/
├── README.md          (this file)
├── math/
│   └── TR-001.math.md
├── json/
│   └── TR-001.json
└── python/
    └── TR-001.python.md
```

## Naming convention

`{RULE_ID}.{type}.{ext}` — Category code + number (TASS-011).

Examples:

- `TR-001.math.md`
- `TR-C001.json`
- `TR-E001.python.md`

Legacy `TREND-*` filenames are deprecated.

## Retrofill guide (기존 rules/ → specs/)

기존 [rules/tr/](../rules/tr/) 문서를 기준으로 specs/를 역생성합니다.

1. **read_project_spec** — 대상 Rule Markdown 확인
2. **convert_to_math_spec** — 수식·조건식·점수식 추출 → `specs/math/`
3. **convert_to_math_spec** — JSON 스키마 생성 → `specs/json/`
4. **generate_python_spec** — 함수명·입력·출력 정의 → `specs/python/`
5. **03_python_implementer** — `specs/python/` 기준으로 `engine/` 구현
6. **05_reviewer_qa** — rules ↔ specs ↔ engine 3-way 일치 검증

## Validation checklist

- [ ] Rule ID가 rules/, specs/math/, specs/json/, specs/python/, engine/에서 동일
- [ ] 점수 범위가 Math Spec과 JSON에 일치
- [ ] PASS/WARN/FAIL 조건이 3개 spec에 동일
- [ ] Python 구현이 specs/python/ 함수 시그니처와 일치
- [ ] 금지 데이터(뉴스, 재무제표 등) 미사용

## Subdirectories

- [math/](math/) — 수학적 정의
- [json/](json/) — AI/런타임 JSON 규격
- [python/](python/) — Python 구현 명세
