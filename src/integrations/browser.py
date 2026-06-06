"""Placeholder browser integration adapter."""

from __future__ import annotations

from src.integrations.base import AdapterResult


def check_browser_adapter() -> AdapterResult:
    return AdapterResult(
        source="browser",
        status="placeholder",
        message="Historical browser automation removed in favor of safe reconstruction.",
    )
