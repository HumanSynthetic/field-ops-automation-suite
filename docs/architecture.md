# Architecture

## Purpose

This repo demonstrates a small public-safe slice of the private `latest-7kauto` family:

- one orchestrator
- one refresh pass that coordinates workflows
- one jobs-reporting workflow
- one price-sync workflow
- one lightweight dashboard
- one shared adapter layer

## Data Flow

1. `scheduler.py` registers the available workflow groups.
2. The scheduler triggers a demonstrative refresh pass.
3. `data_refresh.py` runs representative reporting and transformation workflows.
4. Adapter health is included alongside workflow output.
5. The combined snapshot is rendered through the dashboard as HTML or JSON.

## Main Parts

### Orchestrator

`src/orchestrator/scheduler.py`

- registers workflow tasks
- runs a single demonstrative refresh pass
- assembles a snapshot for the dashboard
- keeps the task model explicit instead of burying flow in one large script

### Workflows

`src/workflows/`

- `jobs_reporting.py`
  - filters and summarizes sample jobs and estimates data
  - mirrors the structured dashboard-oriented branch of the historical family
- `price_sync.py`
  - transforms sample pricing inputs into normalized output
  - stands in for the browser-plus-transform lane from the mature branch
- `data_refresh.py`
  - coordinates both workflows into one backend snapshot
  - records adapter status beside workflow results

### Dashboard

`src/dashboard/app.py`

- serves a small HTML status page using the standard library
- exposes a JSON snapshot route for lightweight inspection
- renders a safe internal-tools style surface without any live backend dependency

### Integrations

`src/integrations/`

- `base.py`
  - shared adapter contracts
- `browser.py`
  - placeholder browser adapter pattern
- `http_api.py`
  - placeholder HTTP adapter pattern

### Storage

`src/storage/sample_data.py`

- reviewed safe fixture data used by the demo workflows
- intentionally small enough to inspect easily during reconstruction

## What Is Intentionally Missing

- credentials
- live endpoints
- customer identities
- employee recipient lists
- machine-specific paths
- private notification transports
