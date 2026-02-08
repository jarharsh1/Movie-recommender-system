# Movie Recommender System

[![CI](https://github.com/jarharsh1/Movie-recommender-system/actions/workflows/ci.yml/badge.svg)](https://github.com/jarharsh1/Movie-recommender-system/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![Code style: PEP8](https://img.shields.io/badge/code%20style-PEP8-green.svg)](https://peps.python.org/pep-0008/)

A **content-based movie recommendation system** that suggests similar movies based on plot, genre, cast, crew, and keywords. Built with Python, scikit-learn, and Streamlit.

## How It Works

The system uses **Natural Language Processing (NLP)** and **cosine similarity** to find movies with similar content:

1. **Feature Extraction** - Combines movie metadata: plot overview, genres, keywords, top 3 cast members, and director
2. **Text Processing** - Applies Porter Stemming and stop-word removal to normalize text
3. **Vectorization** - Converts text features into numerical vectors using `CountVectorizer` (15,000 features)
4. **Similarity Computation** - Calculates cosine distance between all ~4,800 movie vectors
5. **Recommendation** - Returns the top 5 most similar movies with poster images from TMDB

## Project Structure

```
Movie-recommender-system/
├── .github/workflows/ci.yml    # CI/CD pipeline
├── src/recommender/
│   ├── __init__.py
│   ├── engine.py               # Core recommendation logic
│   ├── data_loader.py          # Data loading utilities
│   └── poster_fetcher.py       # TMDB API integration
├── tests/
│   ├── conftest.py             # Shared test fixtures
│   ├── test_engine.py          # Engine unit tests
│   ├── test_data_loader.py     # Data loader tests
│   └── test_poster_fetcher.py  # Poster fetcher tests
├── app.py                      # Streamlit web application
├── Movie Recommender System .ipynb  # ML pipeline notebook
├── Dockerfile                  # Container deployment
├── requirements.txt
├── setup.py
├── CONTRIBUTING.md
└── LICENSE
```

## Quick Start

### Prerequisites

- Python 3.9+
- [TMDB API Key](https://www.themoviedb.org/settings/api) (free)

### Installation

```bash
# Clone the repository
git clone https://github.com/jarharsh1/Movie-recommender-system.git
cd Movie-recommender-system

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Edit `.env` and add your TMDB API key:

```
TMDB_API_KEY=your_api_key_here
```

### Generate Data Files

If `movies.pkl` and `vector_distance.pkl` are not present, run the Jupyter notebook to generate them:

```bash
jupyter notebook "Movie Recommender System .ipynb"
```

Run all cells to produce the pickle files.

### Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### Docker

```bash
# Build the image
docker build -t movie-recommender .

# Run the container
docker run -p 8501:8501 -e TMDB_API_KEY=your_key movie-recommender
```

## Running Tests

```bash
# Run all tests
PYTHONPATH=src pytest tests/ -v

# Run with coverage
PYTHONPATH=src pytest tests/ -v --cov=src/recommender --cov-report=term-missing
```

## Dataset

This project uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) from Kaggle, containing metadata for ~5,000 movies including:

- Plot overviews
- Genres, keywords
- Cast and crew information
- Release dates, ratings, revenue

## Tech Stack

| Component | Technology |
|-----------|-----------|
| ML/NLP | scikit-learn, NLTK, NumPy, pandas |
| Web App | Streamlit |
| API | TMDB (The Movie Database) |
| Testing | pytest, pytest-cov |
| CI/CD | GitHub Actions |
| Containerization | Docker |

## Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
