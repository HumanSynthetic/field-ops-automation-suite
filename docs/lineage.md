# Lineage

## Historical Source Family

This reconstruction is based primarily on:

- `E:\7k data\Latest 7Kauto\CurrentlyDeployed`

Supporting lineage context came from:

- `E:\7k data\Latest 7Kauto\CurrentlyDeployedLEGACY`
- `E:\7k data\Latest 7Kauto\V3`
- `E:\7k data\Latest 7Kauto\V2`

## Public Mapping

### Scheduler Pattern

Historical source:

- `Scheduler.py`

Public target:

- `src/orchestrator/scheduler.py`

Public emphasis:

- task registration
- repeatable orchestration pattern
- snapshot assembly instead of one-off script output

### Backend Refresh Pattern

Historical source:

- `BackEndManager.py`

Public target:

- `src/workflows/data_refresh.py`

Public emphasis:

- grouped refresh execution
- one combined backend result
- adapter status captured beside data output

### Internal Dashboard Pattern

Historical source:

- `SevenKfront.py`
- template files under `templates/`

Public target:

- `src/dashboard/app.py`

Public emphasis:

- internal-tools presentation
- small route surface
- safe status rendering from structured data

### Jobs Reporting Pattern

Historical source:

- `Estimates_open_jobs.py`
- `JEDback.py`

Public target:

- `src/workflows/jobs_reporting.py`

Public emphasis:

- open-work filtering
- estimate-oriented summarization
- JSON-friendly output over email-heavy behavior

### Pricing Or Parts Transformation Pattern

Historical source:

- `HCJSPriceSync.py`
- `OrderPartsManagement.py`
- `AutoPartSystem.py`

Public target:

- `src/workflows/price_sync.py`

Public emphasis:

- catalog normalization
- transformation output suitable for downstream use
- fixture-driven reconstruction instead of vendor-bound automation

## Public Boundary

The public repo preserves the structure and ideas, not the private runtime:

- keep orchestration, transformation, dashboard, and adapter patterns
- remove secrets, recipients, cached data, and vendor-bound selectors
