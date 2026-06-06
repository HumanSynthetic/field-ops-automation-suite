from __future__ import annotations

import json
import unittest

from src.dashboard.app import render_snapshot
from src.orchestrator.scheduler import run_once
from src.workflows.jobs_reporting import build_jobs_report
from src.workflows.price_sync import build_price_sync_report


class DemoWorkflowTests(unittest.TestCase):
    def test_jobs_report_counts_open_jobs_and_estimates(self) -> None:
        report = build_jobs_report()
        self.assertEqual(report["open_job_count"], 2)
        self.assertEqual(report["pending_estimate_count"], 1)
        self.assertEqual(report["owners"], ["dispatcher-a", "dispatcher-b"])

    def test_price_sync_builds_normalized_items(self) -> None:
        report = build_price_sync_report()
        self.assertEqual(report["catalog_version"], "sample-v1")
        self.assertEqual(report["item_count"], 3)
        self.assertEqual(report["items"][0]["list_price"], 16.5)

    def test_run_once_returns_structured_snapshot(self) -> None:
        snapshot = run_once()
        self.assertEqual(snapshot["task_count"], 1)
        self.assertEqual(snapshot["tasks"][0]["name"], "data_refresh")
        self.assertEqual(snapshot["results"]["data_refresh"]["status"], "ok")
        self.assertEqual(snapshot["results"]["data_refresh"]["adapter_count"], 2)

    def test_render_snapshot_outputs_expected_sections(self) -> None:
        snapshot = run_once()
        rendered = render_snapshot(snapshot)
        self.assertIn("Field Ops Automation Suite", rendered)
        self.assertIn("Jobs Reporting", rendered)
        self.assertIn("/snapshot", rendered)

    def test_snapshot_is_json_serializable(self) -> None:
        snapshot = run_once()
        encoded = json.dumps(snapshot)
        self.assertIn("data_refresh", encoded)


if __name__ == "__main__":
    unittest.main()
