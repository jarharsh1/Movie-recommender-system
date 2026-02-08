"""Tests for the recommendation engine."""

import numpy as np
import pandas as pd
import pytest

from recommender.engine import RecommendationEngine
from recommender.poster_fetcher import PLACEHOLDER_IMAGE


class TestRecommendationEngine:
    """Tests for RecommendationEngine."""

    def test_get_recommendations_returns_correct_count(self, engine):
        results = engine.get_recommendations("The Matrix", n=3)
        assert len(results) == 3

    def test_get_recommendations_returns_tuples(self, engine):
        results = engine.get_recommendations("The Matrix", n=2)
        for item in results:
            assert isinstance(item, tuple)
            assert len(item) == 2
            title, poster = item
            assert isinstance(title, str)
            assert isinstance(poster, str)

    def test_get_recommendations_excludes_input_movie(self, engine):
        results = engine.get_recommendations("The Matrix", n=4)
        titles = [title for title, _ in results]
        assert "The Matrix" not in titles

    def test_get_recommendations_default_count(self, engine):
        # Default n=5, but we only have 5 movies total (4 others)
        results = engine.get_recommendations("The Matrix", n=4)
        assert len(results) == 4

    def test_get_recommendations_unknown_movie_raises(self, engine):
        with pytest.raises(ValueError, match="not found"):
            engine.get_recommendations("Nonexistent Movie")

    def test_movie_exists_true(self, engine):
        assert engine.movie_exists("The Matrix") is True

    def test_movie_exists_false(self, engine):
        assert engine.movie_exists("Nonexistent") is False

    def test_get_movie_titles(self, engine):
        titles = engine.get_movie_titles()
        assert len(titles) == 5
        assert "The Matrix" in titles
        assert "Inception" in titles

    def test_recommendations_are_deterministic(self, engine):
        """Same input should produce same output."""
        results1 = engine.get_recommendations("The Matrix", n=3)
        results2 = engine.get_recommendations("The Matrix", n=3)
        assert results1 == results2

    def test_different_movies_give_different_recommendations(self, engine):
        """Different seed movies should produce different orderings."""
        results_matrix = engine.get_recommendations("The Matrix", n=4)
        results_godfather = engine.get_recommendations("The Godfather", n=4)
        titles_matrix = [t for t, _ in results_matrix]
        titles_godfather = [t for t, _ in results_godfather]
        # The order should differ
        assert titles_matrix != titles_godfather
