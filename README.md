# Field Ops Automation Suite

Operational automation and reporting tools rebuilt from a long-running private field and office workflow system.

## Overview

This repo is a sanitized reconstruction inspired by the `latest-7kauto` family found in the `E:\` archive. The original private system evolved across `V2`, `V3`, `CurrentlyDeployedLEGACY`, and `CurrentlyDeployed` branches. This public version keeps the clearest reusable ideas from the mature end of that lineage without carrying forward credentials, customer data, or machine-local glue.

## What This Repo Represents

- scheduler-centered recurring jobs
- operational data handling and transformation
- internal reporting workflows
- browser and API adapter patterns
- a lightweight internal dashboard surface
- software lineage from rough automation toward cleaner systems

## Demo Scope

The public-safe demo focuses on one small but honest slice of the historical system:

- a scheduler that registers recurring workflow groups
- a backend refresh pass that coordinates representative collectors
- a jobs-reporting workflow that summarizes safe fixture data
- a price-sync workflow that normalizes sample catalog entries
- lightweight browser and HTTP adapter placeholders
- a standard-library dashboard with both HTML and JSON views

## Repo Layout

- `docs/architecture.md`
- `docs/lineage.md`
- `docs/reconstruction-boundary.md`
- `src/orchestrator/scheduler.py`
- `src/dashboard/app.py`
- `src/workflows/jobs_reporting.py`
- `src/workflows/price_sync.py`
- `src/workflows/data_refresh.py`
- `src/integrations/`
- `src/storage/sample_data.py`
- `tests/test_demo.py`

## Running The Demo

Run the orchestrator demo:

```bash
python -m src.orchestrator.scheduler
```

Run the lightweight dashboard:

```bash
python -m src.dashboard.app
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

Available routes:

- `/` for the HTML summary
- `/snapshot` for the JSON payload

## Running Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Notes

- this repo is reconstructed from historical private work
- the source family was much larger and messier than what belongs in public
- the goal here is clarity, lineage, and practical structure rather than archival completeness
