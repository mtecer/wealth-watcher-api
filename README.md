# wealth-watcher-api
Organize personal expenses and track your spending, budgets, investments, net worth.

## Setup

```bash
cd wealth-watcher-api

pyenv local 3.11.5

poetry self update

poetry init

poetry shell

poetry add pylint pytest pytest-cov --group dev

poetry add "fastapi[all]"

# Until official SQLModel is updated, using a fork.
# poetry add sqlmodel
poetry add git+https://github.com/honglei/sqlmodel.git

poetry show

poetry install --sync --dry-run
poetry install --sync
```

## Run Uvicorn for Development

```bash
uvicorn main:api --reload
```

## Build & Run Docker Images

```bash
# DOCKER_BUILDKIT=1 docker buildx build --pull -t python:local -f Dockerfile .
docker buildx build --pull -t python:local -f Dockerfile .

docker run -it --rm --name python python:local /bin/bash
docker run -itd -p 8080:8080 --name python python:local

poetry run uvicorn main:api --reload
```

## Build & Run with Docker Compose

```bash
docker compose build ww-api

docker compose up -d ww-api

docker compose down ww-api

docker compose ps
docker compose top
docker compose ls
```

## Test with pytest

```bash
pytest --verbose .

python -m pytest tests -v
```



