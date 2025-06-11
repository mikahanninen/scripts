# Personal Scripts Collection

A collection of useful Python scripts for various tasks.

## Scripts Overview

| Script | Description | Example output |
|--------|-------------|----------------|
| `electricity.py` | Fetches and displays current electricity prices in Finland using the Pörssisähkö API. Shows prices in a color-coded table format (green for low, yellow for medium, red for high prices). | - |
| `git-smart-commit.py` | An AI-powered Git commit message generator that uses GPT-4 to create meaningful commit messages based on staged changes. Requires OpenAI API key. | - |
| `weather.py` | Weather information fetcher that displays current weather conditions, temperature, wind speed, and sunrise/sunset times for a specified city. Uses OpenWeatherMap API. | - |

## Requirements

- Python 3.x
- All required packages are listed in [requirements.txt](requirements.txt)

### Setup

1. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Note: Make sure to activate the virtual environment before running any scripts or installing new packages.

## Environment Variables

Some scripts require API keys to be set as environment variables:

- `OPENWEATHER_API_KEY`: For weather.py
- `OPENAI_API_KEY`: For git-smart-commit.py

## Usage

Each script can be run directly with Python (make sure your virtual environment is activated):

```bash
python electricity.py
python weather.py
python git-smart-commit.py
```

## License

MIT License