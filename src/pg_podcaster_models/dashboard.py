"""Shared dashboard response. All timestamps are Unix epoch seconds."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DashboardSummary:
    """v1 dashboard shell; statistics and ownership claiming come later."""

    generated_at: int
    podcasts: list[Any] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "generated_at": self.generated_at,
            "podcasts": list(self.podcasts),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DashboardSummary":
        if "generated_at" not in data:
            raise ValueError("generated_at is required")
        return cls(
            generated_at=int(data["generated_at"]),
            podcasts=list(data.get("podcasts", [])),
        )
