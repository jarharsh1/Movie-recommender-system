"""Tests for the poster fetcher module."""

from unittest.mock import patch, MagicMock

import pytest

from recommender.poster_fetcher import (
    PosterFetcher,
    PLACEHOLDER_IMAGE,
    TMDB_IMAGE_BASE_URL,
)


class TestPosterFetcher:
    """Tests for PosterFetcher."""

    def test_init_with_api_key(self):
        fetcher = PosterFetcher(api_key="test_key")
        assert fetcher.api_key == "test_key"

    def test_init_without_api_key_returns_placeholder(self):
        fetcher = PosterFetcher(api_key="")
        result = fetcher.fetch_poster(12345)
        assert result == PLACEHOLDER_IMAGE

    @patch("recommender.poster_fetcher.requests.get")
    def test_fetch_poster_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"poster_path": "/abc123.jpg"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        fetcher = PosterFetcher(api_key="test_key")
        result = fetcher.fetch_poster(550)

        assert result == f"{TMDB_IMAGE_BASE_URL}/abc123.jpg"
        mock_get.assert_called_once()

    @patch("recommender.poster_fetcher.requests.get")
    def test_fetch_poster_no_poster_path(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"poster_path": None}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        fetcher = PosterFetcher(api_key="test_key")
        result = fetcher.fetch_poster(550)

        assert result == PLACEHOLDER_IMAGE

    @patch("recommender.poster_fetcher.requests.get")
    def test_fetch_poster_api_error_returns_placeholder(self, mock_get):
        mock_get.side_effect = Exception("Network error")

        fetcher = PosterFetcher(api_key="test_key")
        result = fetcher.fetch_poster(550)

        assert result == PLACEHOLDER_IMAGE

    @patch("recommender.poster_fetcher.requests.get")
    def test_fetch_poster_timeout(self, mock_get):
        import requests

        mock_get.side_effect = requests.Timeout("Request timed out")

        fetcher = PosterFetcher(api_key="test_key")
        result = fetcher.fetch_poster(550)

        assert result == PLACEHOLDER_IMAGE

    def test_fetch_poster_with_env_var(self, monkeypatch):
        monkeypatch.setenv("TMDB_API_KEY", "env_test_key")
        fetcher = PosterFetcher()
        assert fetcher.api_key == "env_test_key"
