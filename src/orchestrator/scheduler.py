"""Minimal orchestrator inspired by the historical Scheduler.py."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Callable

from src.workflows.data_refresh import run_refresh


@dataclass(frozen=True)
class Task:
    name: str
    runner: Callable[[], dict]


def build_tasks() -> list[Task]:
    return [Task(name="data_refresh", runner=run_refresh)]


def run_once() -> dict:
    started_at = datetime.now(timezone.utc).isoformat()
    results: dict[str, dict] = {}
    for task in build_tasks():
        results[task.name] = task.runner()
    return {
        "started_at": started_at,
        "task_count": len(results),
        "tasks": [asdict(task) | {"runner": task.runner.__name__} for task in build_tasks()],
        "results": results,
    }


def main() -> None:
    snapshot = run_once()
    print("Field Ops Automation Suite demo run complete.")
    print(snapshot)


if __name__ == "__main__":
    main()
