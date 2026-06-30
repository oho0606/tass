# TASS-012 : Rule Specification Standard

**Version:** v1.0.0

**Status:** Standard

**Author:** TASS Project

---

# 1. Purpose

This document defines the **mandatory specification** that every Rule in TASS MUST follow.

Every Rule SHALL have the exact same structure. No Rule may omit any required section.

Every Rule MUST be independently testable, explainable, and reusable.

Related: [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md) | [RULE-000 Template](../rules/RULE-000_RULE_TEMPLATE.md)

---

# 2. Rule Specification Structure

Every Rule consists of **18 sections**:

```text
 1. Metadata
 2. Business Definition
 3. Mathematical Definition
 4. Input Specification
 5. Output Specification
 6. Parameters
 7. Preconditions
 8. Calculation Procedure
 9. Decision Logic
10. Edge Cases
11. Dependencies
12. Explainability
13. Performance
14. Unit Test
15. Integration Test
16. Backtest
17. Python Specification
18. JSON Specification
```

---

# 3. Canonical Rule ID Format

Per TASS-012 (primary):

| Type | Format | Example |
|------|--------|---------|
| Atomic | `{CAT}{NNNN}` | `TR0001`, `MA0005` |
| Composite | `{CAT}C{NNN}` | `TRC001` |
| Engine | `{CAT}E{NNN}` | `TRE001` |

**Hyphen aliases** (accepted, normalized at runtime): `TR-001`, `TR-C001`, `TR-E001`

**Legacy aliases** (deprecated): `TREND-001`, etc.

---

# 4. Section Requirements (Summary)

## §1 Metadata

Required: Rule ID, Rule Name, Category, Subcategory, Version, Status, Priority, Weight, Author, Created Date, Updated Date

## §2 Business Definition

Plain English. One objective. No math.

## §3 Mathematical Definition

Exact formulas. No ambiguous wording.

## §4 Input Specification

OHLCV, indicators, parameters, timeframe, historical window.

## §5 Output Specification

Required verdict: **PASS | FAIL | UNKNOWN**

Optional: numeric score, confidence, metadata.

## §6 Parameters

All configurable values declared. Hard-coded values prohibited.

## §7 Preconditions

If preconditions fail → return **UNKNOWN**.

## §8–9 Calculation Procedure & Decision Logic

Deterministic steps and IF/THEN logic.

## §10 Edge Cases

Insufficient history, missing candle, halt, zero volume, NaN, split, etc.

## §11 Dependencies

None or explicit rule IDs. No circular dependencies.

## §12 Explainability

Machine-readable explanation of verdict.

## §13 Performance

Time and space complexity documented.

## §14–16 Tests & Backtest

Unit, integration, backtest metrics defined.

## §17 Python Specification

Every Rule MUST implement (class-based):

```text
initialize()
validate_input()
calculate()
evaluate()
result()
metadata()
```

One Rule · One Class · One File · No global state · No side effects.

## §18 JSON Specification

Required fields: `rule_id`, `rule_name`, `category`, `subcategory`, `version`, `status`, `priority`, `weight`, `description`, `inputs`, `parameters`, `dependencies`, `outputs`

Stored in `specs/json/{RULE_ID}.json`.

---

# 5. Rule Quality Checklist

```text
One Rule · One Fact · One Category · One File · One Class
One Version · One Output · One Responsibility
```

---

# 6. Rule Acceptance Criteria

A Rule is **accepted** only if:

```text
Registry Registered
Specification Complete (18 sections)
Math Defined
Python Implemented
JSON Generated
Unit Test Passed
Integration Test Passed
Backtest Passed
Walk Forward Passed
Explainability Verified
```

Otherwise: **REJECT**

---

# 7. Rule Development Pipeline

```text
Idea → Registry → Specification → Math → Python → JSON
→ Unit Test → Integration Test → Backtest → Walk Forward
→ Production Approval → Production → Monitoring → Retirement
```

---

# 8. AI Development Rules

```text
Never implement without completed Specification.
Never combine multiple facts into one Rule.
Never skip mathematical definitions or testing.
Never use ambiguous wording.
Always produce deterministic output.
Always support explainability, versioning, dependency tracking.
Always follow this Specification exactly.
```

---

# End of Specification

Every present and future Rule MUST comply with TASS-012 before implementation.
