"""A tiny standard-library dashboard for the reconstructed snapshot."""

from __future__ import annotations

import html
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from src.orchestrator.scheduler import run_once


def render_snapshot(snapshot: dict) -> str:
    jobs = snapshot["results"]["data_refresh"]["jobs_reporting"]
    pricing = snapshot["results"]["data_refresh"]["price_sync"]
    adapters = snapshot["results"]["data_refresh"]["adapters"]
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Field Ops Automation Suite</title>
  <style>
    body {{ font-family: sans-serif; margin: 2rem; max-width: 60rem; }}
    .card {{ border: 1px solid #ddd; padding: 1rem; margin-bottom: 1rem; border-radius: 0.5rem; }}
    code {{ background: #f5f5f5; padding: 0.1rem 0.3rem; }}
  </style>
</head>
<body>
  <h1>Field Ops Automation Suite</h1>
  <p>Sanitized reconstruction of a private operations tooling family.</p>
  <div class="card">
    <h2>Run</h2>
    <p><strong>Started:</strong> {html.escape(snapshot["started_at"])}</p>
    <p><strong>Tasks:</strong> {snapshot["task_count"]}</p>
  </div>
  <div class="card">
    <h2>Jobs Reporting</h2>
    <p><strong>Open jobs:</strong> {jobs["open_job_count"]}</p>
    <p><strong>Pending estimates:</strong> {jobs["pending_estimate_count"]}</p>
    <p><strong>Owners:</strong> {", ".join(html.escape(owner) for owner in jobs["owners"])}</p>
  </div>
  <div class="card">
    <h2>Price Sync</h2>
    <p><strong>Items:</strong> {pricing["item_count"]}</p>
    <p><strong>Last catalog version:</strong> <code>{html.escape(pricing["catalog_version"])}</code></p>
  </div>
  <div class="card">
    <h2>Adapters</h2>
    <ul>
      {"".join(f"<li><strong>{html.escape(adapter['source'])}</strong>: {html.escape(adapter['status'])} - {html.escape(adapter['message'])}</li>" for adapter in adapters)}
    </ul>
  </div>
  <p>JSON snapshot: <a href="/snapshot">/snapshot</a></p>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        snapshot = run_once()
        if self.path == "/snapshot":
            payload = json.dumps(snapshot, indent=2).encode("utf-8")
            content_type = "application/json; charset=utf-8"
        else:
            payload = render_snapshot(snapshot).encode("utf-8")
            content_type = "text/html; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("Serving dashboard on http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
