# wealth-watcher-api
Organize personal expenses and track your spending, budgets, investments, net worth.

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



