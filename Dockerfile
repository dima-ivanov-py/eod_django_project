FROM python:3.11.4-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==1.5.1"
COPY ./pyproject.toml ./poetry.lock /
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . .
