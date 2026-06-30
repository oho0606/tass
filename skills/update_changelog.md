# Skill: update_changelog

## 목적

모든 의미 있는 프로젝트 변경사항을 `CHANGELOG.md`에 기록한다. 모든 Agent의 **마지막 필수 작업**이다.

## 사용 시점

- 모든 Agent 작업 완료 후
- Phase 전환 시
- Rule/Spec/Engine 추가·변경 시
- Agent/Skill 시스템 변경 시

## 입력

- 이번 작업의 변경 내용 요약
- 영향받는 파일 목록
- 버전 번호 (Semantic Versioning)

## 출력

- 갱신된 `CHANGELOG.md`

## 실행 절차

### 1. 버전 결정

| 변경 유형 | 버전 |
|-----------|------|
| Breaking change | MAJOR (x.0.0) |
| 새 기능 (Rule, Engine) | MINOR (0.x.0) |
| 버그 수정, 문서 | PATCH (0.0.x) |

### 2. CHANGELOG 형식

```markdown
## [v0.2.0] - YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Fixed
- ...

### Removed
- ...
```

### 3. 기록 규칙

- **Added**: 신규 Rule, Engine, Agent, Skill, spec
- **Changed**: 기존 Rule/Engine 동작 변경
- **Fixed**: 버그 수정
- **Removed**: 폐기 Rule, Deprecated 제거

### 4. 필수 포함 정보

- Rule ID (해당 시)
- Agent 역할 (해당 시)
- Phase 전환 (해당 시)

### 5. 파일 상단에 최신 버전이 오도록 추가 (기존 항목 아래에 append 아님, 최신이 위)

## 체크리스트

- [ ] Semantic Versioning 준수
- [ ] 날짜 기록
- [ ] Added/Changed/Fixed/Removed 분류
- [ ] Rule ID 또는 Engine명 명시 (해당 시)
- [ ] Breaking change 명시 (해당 시)
- [ ] CHANGELOG.md 저장 완료
