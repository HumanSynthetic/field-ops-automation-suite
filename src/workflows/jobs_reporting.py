"""Representative jobs and estimates reporting workflow."""

from __future__ import annotations

from src.storage.sample_data import SAMPLE_JOBS


def build_jobs_report() -> dict:
    open_jobs = [job for job in SAMPLE_JOBS if job["status"] == "open"]
    pending_estimates = [job for job in SAMPLE_JOBS if job["type"] == "estimate"]
    owners = sorted({job["owner"] for job in SAMPLE_JOBS})
    return {
        "open_job_count": len(open_jobs),
        "pending_estimate_count": len(pending_estimates),
        "owners": owners,
    }
