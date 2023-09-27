ARG WORKDIR="/wealth-watcher"

# Builder
FROM python:3.11.5-slim-bookworm AS builder

ARG WORKDIR

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR ${WORKDIR}

RUN pip install poetry --no-cache-dir \
    && poetry config virtualenvs.in-project true

COPY poetry.lock pyproject.toml ${WORKDIR}/
COPY app/ ${WORKDIR}/app/

RUN poetry install --only main

# Runtime
FROM python:3.11.5-slim-bookworm

ARG WORKDIR

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR ${WORKDIR}

COPY --from=builder ${WORKDIR} .

EXPOSE 8080

# ENTRYPOINT [ ".venv/bin/python", "-m", "uvicorn" ]
# CMD [ "main:api", "--host", "0.0.0.0", "--port", "8080" ]
# ENTRYPOINT [ ".venv/bin/uvicorn" ]
# CMD [ "main:api", "--host", "0.0.0.0", "--port", "8080" ]
# CMD [ "main:api", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]
