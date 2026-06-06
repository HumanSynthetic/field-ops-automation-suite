"""Placeholder HTTP API integration adapter."""

from __future__ import annotations

from src.integrations.base import AdapterResult


def check_http_adapter() -> AdapterResult:
    return AdapterResult(
        source="http_api",
        status="placeholder",
        message="Live endpoints and credentials removed in favor of safe fixtures.",
    )
