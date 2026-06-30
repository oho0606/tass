# Rule Structure

This document defines the Rule structure for TASS.

**Official taxonomy:** [docs/TASS-011_Rule_Taxonomy_Specification.md](../docs/TASS-011_Rule_Taxonomy_Specification.md)

**Rule registry:** [rules/registry.yaml](registry.yaml)

## Rule Categories (21 codes)

Every Rule belongs to **exactly one** two-letter category:

| Code | Category |
|------|----------|
| TR | Trend |
| MA | Moving Average |
| PA | Price Action |
| VL | Volume |
| MO | Momentum |
| VO | Volatility |
| MS | Market Structure |
| SR | Support & Resistance |
| BO | Breakout |
| PB | Pullback |
| PT | Pattern |
| CS | Candlestick |
| GP | Gap |
| RK | Risk |
| EN | Entry |
| EX | Exit |
| MR | Market Regime |
| MT | Multi Timeframe |
| CF | Confirmation |
| DQ | Data Quality |
| MTA | Meta Rules |

No Rule may exist outside this taxonomy.

## Rule ID Format (TASS-012 canonical)

```text
{CATEGORY}{NNNN}      Atomic      TR0001, MA0005
{CATEGORY}C{NNN}     Composite   TRC001
{CATEGORY}E{NNN}      Engine      TRE001
```

Hyphen aliases accepted: `TR-001` → `TR0001` (normalized at runtime).

See [docs/TASS-012_Rule_Specification_Standard.md](../docs/TASS-012_Rule_Specification_Standard.md).

## Rule Types

| Type | ID pattern | Description |
|------|------------|-------------|
| Atomic | `{CODE}-{NNN}` | One objective fact |
| Composite | `{CODE}-C{NNN}` | Combines atomic results |
| Engine | `{CODE}-E{NNN}` | Domain engine orchestration |

## Directory Layout

```text
rules/
├── registry.yaml
├── RULE-000_RULE_TEMPLATE.md
├── RULE_STRUCTURE.md
├── tr/                    # TR category rules
│   ├── TR-001_*.md
│   ├── composite/
│   └── engine/
├── ma/                    # MA category (future)
└── ...
```

## Rule Template

Each Rule document must follow [RULE-000_RULE_TEMPLATE.md](RULE-000_RULE_TEMPLATE.md).

Required fields include: Rule ID, Category Code, Subcategory, Name, Status, Version, Purpose, inputs, PASS/WARN/FAIL, scoring, Python interface, tests.

## Rule Validity Requirements

A Rule is valid only if it:

- Belongs to exactly one taxonomy category
- Has a unique Rule ID registered in `registry.yaml`
- Is implementable in Python
- Is measurable, backtestable, explainable
- Is compatible with Gate and Scoring systems
- Has change history

## Gate Priority

Gate Fail eliminates a candidate before final score ranking. No high total score can override a failed Gate.
