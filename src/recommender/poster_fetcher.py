"""TMDB API integration for fetching movie posters."""

import os
import logging

import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
PLACEHOLDER_IMAGE = "https://via.placeholder.com/500x750?text=No+Poster"


class PosterFetcher:
    """Fetches movie poster URLs from the TMDB API."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("TMDB_API_KEY", "")
        if not self.api_key:
            logger.warning(
                "TMDB_API_KEY not set. Poster fetching will return placeholders."
            )

    def fetch_poster(self, movie_id: int) -> str:
        """Fetch the poster URL for a given TMDB movie ID.

        Args:
            movie_id: TMDB movie ID.

        Returns:
            URL string for the movie poster, or a placeholder if unavailable.
        """
        if not self.api_key:
            return PLACEHOLDER_IMAGE

        try:
            url = f"{TMDB_BASE_URL}/movie/{movie_id}"
            response = requests.get(
                url,
                params={"api_key": self.api_key, "language": "en-US"},
                timeout=5,
            )
            response.raise_for_status()
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"{TMDB_IMAGE_BASE_URL}{poster_path}"
            return PLACEHOLDER_IMAGE
        except Exception as e:
            logger.error("Failed to fetch poster for movie %s: %s", movie_id, e)
            return PLACEHOLDER_IMAGE
