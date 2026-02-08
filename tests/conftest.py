"""Shared test fixtures for the movie recommender test suite."""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from recommender.engine import RecommendationEngine
from recommender.poster_fetcher import PosterFetcher


@pytest.fixture
def sample_movies():
    """Create a sample movies DataFrame for testing."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "title": [
                "The Matrix",
                "Inception",
                "Interstellar",
                "The Godfather",
                "Pulp Fiction",
            ],
            "Tags": [
                "sci-fi action hacker chosen one",
                "sci-fi action dream heist",
                "sci-fi space exploration time",
                "crime drama mafia family",
                "crime drama hitman nonlinear",
            ],
        }
    )


@pytest.fixture
def sample_similarity_matrix():
    """Create a sample cosine distance matrix for testing.

    Lower values = more similar in cosine distance.
    Matrix is symmetric with 0 on the diagonal.
    """
    matrix = np.array(
        [
            [0.0, 0.3, 0.5, 0.9, 0.85],  # The Matrix
            [0.3, 0.0, 0.4, 0.8, 0.75],  # Inception
            [0.5, 0.4, 0.0, 0.7, 0.65],  # Interstellar
            [0.9, 0.8, 0.7, 0.0, 0.2],  # The Godfather
            [0.85, 0.75, 0.65, 0.2, 0.0],  # Pulp Fiction
        ]
    )
    return matrix


@pytest.fixture
def mock_poster_fetcher():
    """Create a PosterFetcher that returns placeholder URLs."""
    fetcher = PosterFetcher(api_key="")
    return fetcher


@pytest.fixture
def engine(sample_movies, sample_similarity_matrix, mock_poster_fetcher):
    """Create a RecommendationEngine with test data."""
    return RecommendationEngine(
        sample_movies, sample_similarity_matrix, mock_poster_fetcher
    )
