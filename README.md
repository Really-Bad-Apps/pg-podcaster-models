# pg-podcaster-models

Shared data models for the Podcast Guru podcaster portal (podcaster.podcastguru.io).

## Installation

```bash
pip install git+https://github.com/Really-Bad-Apps/pg-podcaster-models.git
```

### As a dependency in pyproject.toml
```toml
dependencies = [
    # TOKEN-FREE URL — never embed {env:CR_PAT} here. hatchling expands it at
    # wheel build time and bakes the live PAT into .dist-info/METADATA
    # Requires-Dist, leaking a credential into every published image.
    "pg-podcaster-models @ git+https://github.com/Really-Bad-Apps/pg-podcaster-models.git",
]
```

### As a dependency in requirements.txt
```
pg-podcaster-models @ git+https://github.com/Really-Bad-Apps/pg-podcaster-models.git
```

## Usage

```python
from pg_podcaster_models import DashboardSummary

summary = DashboardSummary(generated_at=1700000000)
print(summary.to_dict())  # {"generated_at": 1700000000, "podcasts": []}
```

`DashboardSummary` is shared by the backend, Python API client, and MCP
server. The TypeScript client mirrors its wire shape. v1 returns an empty
podcast list; `generated_at` is an integer Unix timestamp in seconds.

## Development

### Setup

> **Note (Python 3.13+):** `python3 -m venv .` writes a `.gitignore` with `*`
> into the venv root, which is the project root under this convention — so
> re-creating the venv here **overwrites this project's `.gitignore`**. If you
> re-create the venv later, restore the tracked file immediately:
> `git checkout .gitignore`.

```bash
# Create virtual environment
python3 -m venv .

# Activate virtual environment
source bin/activate

# Install dependencies
pip install --upgrade -r requirements.txt
pip install -e .

# Run tests
pytest
```

## Conventions

- All date/time fields are unix timestamps (`int` epoch seconds), never `datetime`.
- Every function has type hints for parameters and return type.
- Models are plain dataclasses; no ORM, no framework imports.

## License

MIT License

## Author

Jason Mazza
