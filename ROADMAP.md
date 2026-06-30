# TASS Roadmap

Post-v1.0 product direction for the Technical Analysis Scoring System.

## v1.0 (General Availability) — 2026-06-30

Phase 6 deliverables completed: data cache validation, recommendation tuning, Docker deployment,
daily automation, production env separation, extended CI, and documentation.

## v1.1 — Real-time & Broker Integration

- KIS Open API live market data (replace Yahoo delayed feed)
- Kiwoom API adapter (optional second broker)
- WebSocket streaming for Dashboard market status
- Intraday picks refresh (pre-market / post-close)

## v1.2 — On-Demand Viewer Experience

- Recent picks history and quick compare UX
- Manual refresh + snapshot-first viewing flow
- Explainable reason readability improvements
- Lightweight local 운영 중심 (no notification pipeline)

## v1.3 — Full Engine Mode

- Disable MVP mode by default (`mvp_mode: false`)
- Full 16-domain scoring (1000-point scale) in production
- Re-tune `recommendation_v1.yaml` for full-scale thresholds
- Expanded KRX universe (KOSPI + KOSDAQ full listings)

## v2.0 — Optional Platform (If Needed)

- Multi-user auth (JWT + API keys) — optional
- PostgreSQL-backed user preferences — optional
- Sentry APM and audit logging hardening
- Mobile companion app — optional

## Research Backlog

- ML-assisted probability calibration from backtest outcomes
- Sector rotation and market regime adaptive thresholds
- Options flow and foreign investor data integration (DART)
- Walk-forward optimization for rule parameters
