# TASS Frontend (TASS-040)

Next.js App Router dashboard for TASS analysis results.

## Stack

- Next.js 16, TypeScript, Tailwind CSS
- TanStack Query (server state), Zustand (UI state)
- ECharts (Domain Radar), TradingView Lightweight Charts (OHLCV)
- Types generated from FastAPI OpenAPI (`openapi-typescript`)

## Quick Start

```bash
# Terminal 1 — API
cd ..
pip install -e ".[api]"
tass api

# Terminal 2 — Frontend
cp .env.local.example .env.local
npm install
npm run dev
```

Open http://localhost:3000

## API Type Sync

After changing FastAPI Pydantic models:

```bash
npm run generate:api
```

This exports `openapi.json` from the running FastAPI app and regenerates `src/lib/api/schema.d.ts`.

## Pages

| Route | Description |
|-------|-------------|
| `/` | Dashboard — market SSE, system health, picks preview |
| `/picks` | Today's Top 20 cards |
| `/stock/[code]` | Explainable AI, radar chart, price chart |
| `/backtest` | Backtest summary + searchable ranking table |

## E2E Tests

```bash
npm install -D @playwright/test
npx playwright install chromium
npx playwright test
```

## Principles

- **Frontend does not compute** — all scores, rules, and indicators come from the API
- Dark mode by default (trading UI)
- Responsive: cards on mobile, tables/charts on desktop
