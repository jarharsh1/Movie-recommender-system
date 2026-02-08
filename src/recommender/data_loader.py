"""Data loading utilities for the movie recommender system."""

import os
import pickle
from pathlib import Path

import pandas as pd


class DataLoader:
    """Loads and manages pre-computed movie data and similarity matrices."""

    def __init__(self, data_dir: str = None):
        if data_dir is None:
            data_dir = Path(__file__).resolve().parent.parent.parent
        self.data_dir = Path(data_dir)

    def load_movies(self) -> pd.DataFrame:
        """Load the movies DataFrame from pickle file."""
        movies_path = self.data_dir / "movies.pkl"
        if not movies_path.exists():
            raise FileNotFoundError(
                f"movies.pkl not found at {movies_path}. "
                "Run the Jupyter notebook first to generate it."
            )
        with open(movies_path, "rb") as f:
            return pickle.load(f)

    def load_similarity_matrix(self):
        """Load the pre-computed similarity matrix from pickle file."""
        similarity_path = self.data_dir / "vector_distance.pkl"
        if not similarity_path.exists():
            raise FileNotFoundError(
                f"vector_distance.pkl not found at {similarity_path}. "
                "Run the Jupyter notebook first to generate it."
            )
        with open(similarity_path, "rb") as f:
            return pickle.load(f)

    def get_movie_titles(self, movies: pd.DataFrame) -> list:
        """Extract sorted list of movie titles."""
        return sorted(movies["title"].values.tolist())
