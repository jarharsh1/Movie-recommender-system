"""Tests for the data loader module."""

import os
import pickle
import tempfile

import numpy as np
import pandas as pd
import pytest

from recommender.data_loader import DataLoader


class TestDataLoader:
    """Tests for DataLoader."""

    def test_load_movies_from_valid_path(self, sample_movies, tmp_path):
        # Save test data
        movies_path = tmp_path / "movies.pkl"
        with open(movies_path, "wb") as f:
            pickle.dump(sample_movies, f)

        loader = DataLoader(data_dir=str(tmp_path))
        loaded = loader.load_movies()
        assert isinstance(loaded, pd.DataFrame)
        assert len(loaded) == len(sample_movies)
        assert list(loaded.columns) == list(sample_movies.columns)

    def test_load_movies_file_not_found(self, tmp_path):
        loader = DataLoader(data_dir=str(tmp_path))
        with pytest.raises(FileNotFoundError, match="movies.pkl not found"):
            loader.load_movies()

    def test_load_similarity_matrix_from_valid_path(
        self, sample_similarity_matrix, tmp_path
    ):
        sim_path = tmp_path / "vector_distance.pkl"
        with open(sim_path, "wb") as f:
            pickle.dump(sample_similarity_matrix, f)

        loader = DataLoader(data_dir=str(tmp_path))
        loaded = loader.load_similarity_matrix()
        assert isinstance(loaded, np.ndarray)
        np.testing.assert_array_equal(loaded, sample_similarity_matrix)

    def test_load_similarity_matrix_file_not_found(self, tmp_path):
        loader = DataLoader(data_dir=str(tmp_path))
        with pytest.raises(FileNotFoundError, match="vector_distance.pkl not found"):
            loader.load_similarity_matrix()

    def test_get_movie_titles(self, sample_movies):
        loader = DataLoader()
        titles = loader.get_movie_titles(sample_movies)
        assert isinstance(titles, list)
        assert len(titles) == 5
        # Should be sorted
        assert titles == sorted(titles)

    def test_default_data_dir(self):
        loader = DataLoader()
        assert loader.data_dir.exists()
