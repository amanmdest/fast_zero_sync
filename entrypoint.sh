#!/bin/sh

poetry run alembic upgrade head

poetry run fastapi run fast_zero/app.py --host 0.0.0.0