# Kairo Kanban

Kairo centraliza metodologia e execução em um único ambiente digital.

## Table of Contents

- [Installation](#installation)
- [Docker](#docker)
- [Tailwind](#tailwind)
- [Celery](#celery)
- [License](#license)

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install the dependencies.
4. Set up the database.

```shell
pip install -r requirements.txt
python manage.py migrate
```

## Docker

Para instanciar os bancos do Postgres (Django) e Redis (Celery) em MODO DEV.

```shell
docker-compose up -d
```

## Tailwind

v4.2.1 Latest

```shell
npm run watch:css
```

## Celery

```shell
celery -A config worker -l info
```
