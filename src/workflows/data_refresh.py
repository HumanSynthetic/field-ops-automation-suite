"""Backend refresh coordinator inspired by BackEndManager.py."""

from __future__ import annotations

from src.integrations.browser import check_browser_adapter
from src.integrations.http_api import check_http_adapter
from src.workflows.jobs_reporting import build_jobs_report
from src.workflows.price_sync import build_price_sync_report


def run_refresh() -> dict:
    adapters = [
        check_browser_adapter().as_dict(),
        check_http_adapter().as_dict(),
    ]
    return {
        "status": "ok",
        "adapter_count": len(adapters),
        "adapters": adapters,
        "jobs_reporting": build_jobs_report(),
        "price_sync": build_price_sync_report(),
    }
