import pytest

from pg_podcaster_models import DashboardSummary


def test_dashboard_round_trip() -> None:
    payload = {"generated_at": 1700000000, "podcasts": []}
    assert DashboardSummary.from_dict(payload).to_dict() == payload


def test_dashboard_requires_timestamp_and_has_independent_lists() -> None:
    with pytest.raises(ValueError, match="generated_at"):
        DashboardSummary.from_dict({})
    first = DashboardSummary(generated_at=1)
    second = DashboardSummary(generated_at=2)
    first.podcasts.append({"title": "Example"})
    assert second.podcasts == []
