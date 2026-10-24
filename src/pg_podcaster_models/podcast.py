"""Minimal public wire models for the podcast information page."""

from dataclasses import asdict, dataclass
from typing import Any, Literal


@dataclass
class PodcastInfo:
    id: str
    name: str
    artwork_url: str | None = None
    overview: dict[str, Any] | None = None


@dataclass
class PodcastLookup:
    status: Literal["found", "pending"]
    podcast: PodcastInfo | None = None
    retry_after: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PodcastLookup":
        status = data["status"]
        if status == "found":
            podcast = data["podcast"]
            return cls(status="found", podcast=PodcastInfo(
                id=podcast["id"], name=podcast["name"], artwork_url=podcast.get("artwork_url"),
                overview=podcast.get("overview"),
            ))
        if status == "pending":
            return cls(status="pending", retry_after=int(data.get("retry_after") or 3))
        raise ValueError("Unknown podcast lookup status")
