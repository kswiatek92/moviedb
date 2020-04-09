FROM python:3.8


WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi


COPY . /app

ENV PYTHONUNBUFFERED 1
ENV PROCESSES 4


CMD ["python", "/app/runserver.py"]
