"""Representative pricing transformation workflow."""

from __future__ import annotations

from src.storage.sample_data import SAMPLE_PRICE_ITEMS


def build_price_sync_report() -> dict:
    normalized = [
        {
            "sku": item["sku"],
            "list_price": round(item["base_price"] * item["markup"], 2),
        }
        for item in SAMPLE_PRICE_ITEMS
    ]
    return {
        "catalog_version": "sample-v1",
        "item_count": len(normalized),
        "items": normalized,
    }
