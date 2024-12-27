FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

CMD ["bash", "-c", "poetry run alembic upgrade head && poetry run python main.py"]
