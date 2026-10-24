import pytest

from pg_podcaster_models import PodcastInfo, PodcastLookup


def test_lookup_roundtrip() -> None:
    for lookup in [PodcastLookup("found", PodcastInfo("123", "Example")), PodcastLookup("pending", retry_after=4)]:
        assert PodcastLookup.from_dict(lookup.to_dict()) == lookup


def test_lookup_rejects_unknown_status() -> None:
    with pytest.raises(ValueError):
        PodcastLookup.from_dict({"status": "unexpected"})


def test_optional_overview_roundtrips_without_inventing_zero() -> None:
    raw = {"status": "found", "podcast": {"id": "123", "name": "Example",
        "overview": {"catalog": {"episode_count": 0, "latest_episode": None},
                     "op3": {"status": "not_tracked"}}}}
    result = PodcastLookup.from_dict(raw)
    assert result.to_dict()["podcast"]["overview"] == raw["podcast"]["overview"]
