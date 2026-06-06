"""Reviewed safe fixture data for demo workflows."""

SAMPLE_JOBS = [
    {"id": "job-1001", "status": "open", "type": "job", "owner": "dispatcher-a"},
    {"id": "job-1002", "status": "open", "type": "estimate", "owner": "dispatcher-b"},
    {"id": "job-1003", "status": "closed", "type": "job", "owner": "dispatcher-a"},
]

SAMPLE_PRICE_ITEMS = [
    {"sku": "filter-20x20x1", "base_price": 10.0, "markup": 1.65},
    {"sku": "capacitor-45-5", "base_price": 18.0, "markup": 1.5},
    {"sku": "contact-kit-a", "base_price": 24.0, "markup": 1.4},
]
