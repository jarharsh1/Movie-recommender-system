"""Movie Recommender System - Content-based recommendation engine."""

from recommender.engine import RecommendationEngine
from recommender.data_loader import DataLoader
from recommender.poster_fetcher import PosterFetcher

__all__ = ["RecommendationEngine", "DataLoader", "PosterFetcher"]
__version__ = "1.0.0"
