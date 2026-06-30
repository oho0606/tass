# TASS AI Development Specification v1.0

## Project Name

TASS (Technical Analysis Scoring Specification)

## AI Role

The AI is not a simple code generator.

The AI acts as a senior development team for TASS:

- Chief Software Architect
- Senior Quant Developer
- Senior Backend Engineer
- Senior Frontend Engineer
- Senior Python Engineer
- Senior Technical Writer
- Senior QA Engineer

The AI must understand the entire project and maintain consistency across architecture, documentation, rules, implementation, tests, and reports.

## Project Vision

TASS is not a chart analysis program.

TASS is an AI-based technical analysis stock recommendation platform.

The final goal is not for users to search stocks manually. The final goal is for users to visit the website and automatically receive today's most favorable stock recommendations.

## User Journey

```text
Visit site
↓
Today's Picks
↓
TOP 20 recommended stocks
↓
Click stock
↓
Review recommendation reason
↓
Decide whether to buy
```

This is the core service.

Complex chart analysis is performed by the system.

## Core Philosophy

TASS does not predict the future.

TASS selects stocks with favorable probability.

```text
Prediction: No
Probability: Yes
Opinion: No
Data: Yes
Emotion: No
Rule: Yes
```

## Allowed Data

- OHLCV
- Volume
- Moving averages
- ATR
- RSI
- MACD
- OBV
- Bollinger Bands
- Fibonacci
- Dow Theory
- Granville Rules
- Wyckoff Method
- Turtle Trading
- ADX
- DMI
- VWAP
- Relative Strength
- Other technical analysis data

## Forbidden Data

- News
- Disclosures
- Earnings
- Politics
- SNS
- YouTube
- Communities
- Analyst opinions
- Themes
- Rumors

## System Structure

```text
User
↓
Frontend
↓
Backend API
↓
TASS Engine
↓
Scoring Engine
↓
Database
↓
Report Engine
↓
Recommended Stocks
```

## Recommendation Method

```text
2700 stocks
↓
Primary filter
↓
Liquidity
↓
Volume
↓
Market environment
↓
Base trend
↓
100-300 candidates
↓
Detailed analysis
↓
Dow Theory
↓
Granville Rules
↓
Wyckoff Method
↓
OBV
↓
MACD
↓
RSI
↓
Bollinger Bands
↓
ATR
↓
Relative Strength
↓
Final score
↓
Confidence
↓
TOP 20
```

## Scoring System

The total score is 1000 points.

Scoring areas:

- Market environment
- Trend
- Moving average
- Volume
- Momentum
- Volatility
- Risk management

Each area is calculated using Rule-based logic.

Every Rule must be:

- Implementable
- Measurable
- Backtestable
- Explainable
- Assigned a Rule ID
- Managed with change history

## Gate System

Gate has priority over total score.

Examples:

```text
Weak market
↓
Gate Fail
↓
Eliminated
```

```text
Insufficient volume
↓
Gate Fail
↓
Eliminated
```

```text
Insufficient liquidity
↓
Gate Fail
↓
Eliminated
```

```text
Long-term downtrend
↓
Gate Fail
↓
Eliminated
```

## Confidence

Confidence is calculated separately from the total score.

Confidence combines:

- Trend alignment
- Volume alignment
- Momentum alignment
- Volatility suitability
- Multi-timeframe alignment

## Project Structure

```text
TASS/
├── README.md
├── CHANGELOG.md
├── PROJECT_SPEC.md
├── AI_CONTEXT.md
├── docs/
├── rules/
├── backend/
├── frontend/
├── engine/
├── backtest/
├── database/
├── config/
├── tests/
├── scripts/
└── prompts/
```

## AI Collaboration Principles

TASS must not depend on a specific AI.

The following AI tools must be able to continue the project by reading the same documents:

- Cursor AI
- Claude Code
- Codex
- Gemini
- GitHub Copilot
- Other AI tools

Every new AI must read these files first:

1. `PROJECT_SPEC.md`
2. `AI_CONTEXT.md`
3. `CHANGELOG.md`
4. `README.md`

## Development Principles

1. Design first.
2. Code is only the implementation of design.
3. Every Rule has a Rule ID.
4. Every Rule must be backtestable.
5. Every Rule must be implementable in Python.
6. Every Rule must be explainable.
7. Every Rule has a change history.
8. Every change must be validated with data.
9. Statistics come before intuition.
10. Structure comes before additional features.

## AI Behavior Rules

AI must never arbitrarily change the project structure.

AI must not write code that conflicts with existing Rules.

AI must always review existing documents before development.

AI must check consistency with the current structure before adding any new feature.

## Current Project Phase

Current phase: **MVP Implementation + Phase 6 Product Validation** (v1.0-rc1).

Current work:

- MVP operational pipeline (Trend + MA + Volume, 500-point scale)
- Rule SSOT retrofill for MVP subset (`config/mvp_operational_rules.yaml`)
- KRX universe expansion and cache validation
- Phase 6: recommendation tuning, daily pipeline, Docker/CI

Allowed:

- Engine, API, tests, scripts, frontend (BFF only — no client-side scoring)
- MVP rule SSOT and backtest validation

Deferred to v1.3+:

- Full Engine mode (`mvp_mode: false`, 1000-point scale) as default
- Production multi-user deployment

## Final Goal

TASS is not a technical analysis program.

TASS is a technical analysis stock recommendation platform that AI can understand, developers can implement, and users can use by reviewing only recommended stocks.

The first screen users see must be `Today's Picks`.
