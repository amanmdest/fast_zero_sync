#!/bin/sh

poetry run alembic upgrade head

# poetry run fastapi run fast_zero/app.py --host 0.0.0.0
poetry run uvicorn --host 0.0.0.0 --port 8000 fast_zero.app:app