# Development Roadmap

This roadmap starts from the Project Foundation phase.

## Phase 0: Project Foundation

Goal: establish structure before implementation.

Status: **Complete**

## Phase 1: Core Specification

Goal: define what TASS is before building it.

Status: **Complete** (TASS-001–010 drafted; MVP-aligned notes added v1.0-rc1)

## Phase 2: Rule Specification

Goal: define the first measurable Rule set.

Status: **Complete** (TASS-011–027 frozen catalogs; 1,235 rules in registry)

## Phase 3: Backtest Specification

Goal: define how Rules are validated.

Status: **Complete** (TASS-031 Backtest Engine frozen)

## Phase 4: System Architecture Specification

Goal: prepare implementation without writing production code prematurely.

Status: **Complete** (TASS-032 Application Layer frozen; API + frontend scaffold)

## Phase 5: Minimal Implementation

Goal: implement only the smallest version that matches the approved specifications.

Status: **Complete** (MVP 3-domain pipeline, 1,160+ rule evaluators, API, frontend)

## Phase 6: Product Validation

Goal: validate that the platform serves the user goal.

Status: **Complete** (v1.0.0, 2026-06-30)

Delivered:

- MVP Rule SSOT (26 operational rules) resolved with adoption workflow
- Universe expansion (59 liquid KRX names)
- Cache validation and daily pipeline
- Recommendation threshold tuning and regime baseline validation
- Docker/CI/E2E scaffold

Exit criteria:

- Users can access the site and understand why each TOP 20 stock was recommended.
- MVP rules pass backtest adoption workflow.
