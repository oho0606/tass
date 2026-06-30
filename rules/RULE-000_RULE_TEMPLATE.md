# RULE-000 : Rule Specification Template

**Standard:** TASS-012 Rule Specification Standard v1.0

**Taxonomy:** TASS-011

**Version:** v2.0.0

**Status:** Standard

---

Use this template for **every** Rule. All 18 sections are **mandatory**. Do not omit any section.

---

# 1. Metadata

| Field | Value |
|-------|-------|
| Rule ID | TR0001 |
| Rule Name | Higher High |
| Category | TR (Trend) |
| Subcategory | Direction |
| Version | 1.0.0 |
| Status | Draft |
| Priority | High |
| Weight | 1.00 |
| Author | TASS Project |
| Created Date | YYYY-MM-DD |
| Updated Date | YYYY-MM-DD |

---

# 2. Business Definition

**Purpose:** (Plain English, one objective, no mathematical expressions.)

Example: Determine whether today's swing high is higher than the previous confirmed swing high.

---

# 3. Mathematical Definition

(Exact formulas only. No ambiguous wording.)

```text
CurrentSwingHigh > PreviousSwingHigh
```

---

# 4. Input Specification

| Input | Type | Required |
|-------|------|----------|
| OHLCV | DataFrame | Yes |
| high | Series | Yes |
| close | Series | Yes |
| volume | Series | Optional |
| Timeframe | Daily | Yes |
| Historical Window | 40 bars | Yes |

---

# 5. Output Specification

**Verdict (required):** PASS | FAIL | UNKNOWN

**Optional:** Numeric Score (0–20), Confidence delta, Metadata dict

---

# 6. Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| lookback | 40 | Trading days window |
| pivot_strength | 3 | Pivot detection strength |
| min_hh_count | 2 | Minimum higher-high count |

Hard-coded values are **prohibited** in implementation.

---

# 7. Preconditions

| Precondition | Failure verdict |
|--------------|-----------------|
| Minimum N candles available | UNKNOWN |
| Required columns present | UNKNOWN |
| No critical NaN in price | UNKNOWN |

---

# 8. Calculation Procedure

```text
Step 1: Extract lookback window
Step 2: Detect pivot highs
Step 3: Count higher-high sequences
Step 4: Compute quality metrics
Step 5: Map to verdict and score
```

Every step must be deterministic.

---

# 9. Decision Logic

```text
IF preconditions_fail THEN UNKNOWN
ELSE IF hh_count >= min_hh_count AND quality >= threshold THEN PASS
ELSE IF hh_count >= min_hh_count AND quality >= warn_threshold THEN PASS (low score)
ELSE FAIL
```

Complex logic must be decomposed into Atomic Rules.

---

# 10. Edge Cases

| Case | Expected behavior |
|------|-------------------|
| Insufficient history | UNKNOWN |
| Missing candle | UNKNOWN |
| Trading halt | UNKNOWN |
| Zero volume | Evaluate with volume_ok=false |
| NaN in OHLC | UNKNOWN |
| Stock split | Use adjusted OHLCV |

---

# 11. Dependencies

```text
None
```

or

```text
Depends On: TR0001, TR0002
```

Circular dependency is prohibited.

---

# 12. Explainability

Machine-readable explanation example:

```json
{
  "verdict": "PASS",
  "because": {
    "current_swing_high": 105.22,
    "previous_swing_high": 102.81,
    "hh_count": 3
  }
}
```

---

# 13. Performance

| Metric | Value |
|--------|-------|
| Time Complexity | O(n) |
| Space Complexity | O(1) |

---

# 14. Unit Test

Minimum scenarios:

- Normal case (uptrend → PASS)
- Boundary case (exactly min_hh_count)
- Invalid input (empty DataFrame → UNKNOWN)
- Missing data (short history → UNKNOWN)
- Equal values (flat highs)
- Extreme values (spike)

Target: 100% PASS

---

# 15. Integration Test

Verify compatibility with:

- Rule Engine
- Composite Rule Engine
- Master Score Engine
- Backtest Engine
- Explainability Engine

---

# 16. Backtest

| Field | Value |
|-------|-------|
| Dataset | KOSPI + KOSDAQ |
| Period | 10–15 years |
| Timeframe | Daily |
| Metrics | Win Rate, PF, Sharpe, Sortino, CAGR, MDD, Trade Count |

---

# 17. Python Specification

**Module:** `engine.rules.tr.tr0001_higher_high`

**Class:** `TR0001HigherHighRule`

**Methods (required):**

```python
def initialize(self, parameters: dict) -> None: ...
def validate_input(self, df: pd.DataFrame) -> bool: ...
def calculate(self, df: pd.DataFrame) -> dict: ...
def evaluate(self, df: pd.DataFrame) -> RuleVerdict: ...
def result(self) -> RuleResult: ...
def metadata(self) -> dict: ...
```

One Rule · One Class · One File · No global state · No side effects.

---

# 18. JSON Specification

File: `specs/json/TR0001.json`

Required fields: `rule_id`, `rule_name`, `category`, `subcategory`, `version`, `status`, `priority`, `weight`, `description`, `inputs`, `parameters`, `dependencies`, `outputs`

---

# Rule Quality Checklist

- [ ] One Rule, one fact, one category
- [ ] One file, one class, one version
- [ ] Registered in `rules/registry.yaml`
- [ ] All 18 sections complete
- [ ] Math defined
- [ ] Python + JSON implemented
- [ ] Unit + integration tests pass
- [ ] Explainability verified

---

# Change History

| Version | Date | Change |
|---------|------|--------|
| 2.0.0 | YYYY-MM-DD | TASS-012 18-section standard |
