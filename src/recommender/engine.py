"""Core recommendation engine using content-based filtering."""

import logging
from typing import List, Tuple

import pandas as pd
import numpy as np

from recommender.poster_fetcher import PosterFetcher

logger = logging.getLogger(__name__)


class RecommendationEngine:
    """Content-based movie recommendation engine using cosine similarity."""

    def __init__(
        self,
        movies: pd.DataFrame,
        similarity_matrix: np.ndarray,
        poster_fetcher: PosterFetcher = None,
    ):
        self.movies = movies
        self.similarity_matrix = similarity_matrix
        self.poster_fetcher = poster_fetcher or PosterFetcher()

    def get_recommendations(
        self, movie_title: str, n: int = 5
    ) -> List[Tuple[str, str]]:
        """Get movie recommendations based on content similarity.

        Args:
            movie_title: Title of the movie to base recommendations on.
            n: Number of recommendations to return.

        Returns:
            List of (title, poster_url) tuples for recommended movies.

        Raises:
            ValueError: If the movie title is not found in the dataset.
        """
        matches = self.movies[self.movies["title"] == movie_title]
        if matches.empty:
            raise ValueError(f"Movie '{movie_title}' not found in dataset.")

        index = matches.index[0]
        distances = list(enumerate(self.similarity_matrix[index]))
        distances = sorted(distances, reverse=True, key=lambda x: x[1])

        recommendations = []
        for idx, _ in distances:
            if idx == index:
                continue
            if len(recommendations) >= n:
                break
            movie = self.movies.iloc[idx]
            poster_url = self.poster_fetcher.fetch_poster(movie.id)
            recommendations.append((movie.title, poster_url))

        return recommendations

    def get_movie_titles(self) -> List[str]:
        """Return all available movie titles."""
        return self.movies["title"].values.tolist()

    def movie_exists(self, title: str) -> bool:
        """Check if a movie exists in the dataset."""
        return not self.movies[self.movies["title"] == title].empty
