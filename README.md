# wealth-watcher-api
Organize personal expenses and track your spending, budgets, investments, net worth.

## Setup

```bash
cd wealth-watcher-api

pyenv local 3.11.5

poetry self update

poetry init

poetry shell

poetry add pylint --group dev
poetry add "fastapi[all]"

poetry show

poetry install --sync --dry-run
poetry install --sync
```

## Run Uvicorn for Development

```bash
uvicorn main:api --reload
```