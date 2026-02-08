# Contributing to Movie Recommender System

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/<your-username>/Movie-recommender-system.git
   cd Movie-recommender-system
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Development Workflow

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Run the test suite:
   ```bash
   PYTHONPATH=src pytest tests/ -v
   ```
4. Commit your changes with a descriptive message
5. Push to your fork and open a Pull Request

## Code Standards

- Follow PEP 8 style guidelines
- Add docstrings for all public functions and classes
- Write tests for new functionality
- Keep functions focused and under 50 lines where possible

## Running Tests

```bash
# Run all tests
PYTHONPATH=src pytest tests/ -v

# Run with coverage report
PYTHONPATH=src pytest tests/ -v --cov=src/recommender --cov-report=term-missing

# Run a specific test file
PYTHONPATH=src pytest tests/test_engine.py -v
```

## Reporting Issues

- Use the GitHub issue tracker
- Include steps to reproduce the issue
- Include your Python version and OS
- Attach error logs if applicable

## Pull Request Guidelines

- Keep PRs focused on a single change
- Update documentation if needed
- Ensure all tests pass
- Add a clear description of what the PR does and why
