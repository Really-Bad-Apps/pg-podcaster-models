"""
Shared data models for the Podcast Guru podcaster portal (podcaster.podcastguru.io).
"""

from .dashboard import DashboardSummary
from .podcast import PodcastInfo, PodcastLookup

__version__ = "0.0.4"

__all__ = ["DashboardSummary", "PodcastInfo", "PodcastLookup"]
