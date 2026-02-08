"""Streamlit web application for the Movie Recommender System."""

import sys
from pathlib import Path

import streamlit as st

# Add src to path for module imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from recommender.data_loader import DataLoader
from recommender.engine import RecommendationEngine
from recommender.poster_fetcher import PosterFetcher

# Page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
)


@st.cache_resource
def load_engine():
    """Load data and initialize the recommendation engine (cached)."""
    loader = DataLoader()
    movies = loader.load_movies()
    similarity = loader.load_similarity_matrix()
    fetcher = PosterFetcher()
    return RecommendationEngine(movies, similarity, fetcher)


def main():
    st.header("Movie Recommender System")
    st.markdown(
        "Select a movie you enjoy, and we'll recommend 5 similar movies based on "
        "genre, cast, crew, keywords, and plot similarity."
    )

    try:
        engine = load_engine()
    except FileNotFoundError as e:
        st.error(str(e))
        return

    movie_list = engine.get_movie_titles()
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list,
    )

    if st.button("Show Recommendations"):
        try:
            with st.spinner("Finding similar movies..."):
                recommendations = engine.get_recommendations(selected_movie)

            cols = st.columns(5)
            for col, (title, poster_url) in zip(cols, recommendations):
                with col:
                    st.text(title)
                    st.image(poster_url, use_container_width=True)

        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
