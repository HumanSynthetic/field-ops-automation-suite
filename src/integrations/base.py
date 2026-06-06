"""Shared adapter contracts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AdapterResult:
    source: str
    status: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {
            "source": self.source,
            "status": self.status,
            "message": self.message,
        }
