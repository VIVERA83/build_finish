FROM python:3.12.3-slim-bullseye

WORKDIR build_finish

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UVICORN_WORKERS=1

ENV PORT=8008
ENV HOST=0.0.0.0
ENV UVICORN_ARGS "core.setup:setup_app --host $HOST --port $PORT --workers $UVICORN_WORKERS"

# Settings for PostgresSQL database connections
ENV POSTGRES_DB=""
ENV POSTGRES_USER=""
ENV POSTGRES_PASSWORD=""
ENV POSTGRES_HOST="host.docker.internal"
ENV POSTGRES_PORT=""
ENV POSTGRES_SCHEMA=""

COPY build_finish .

RUN echo "Внимание: не забудьте указать актуальные переменные среды для подключения к базе данных Postgresql".
RUN echo "Пример запуска контейнера: docker run --rm -it -p 5432:5432 -e POSTGRES_DB=test_db -e POSTGRES_USER=test_user -e POSTGRES_PASSWORD=test_pass -e -e POSTGRES_PORT=5432 POSTGRES_SCHEMA=postgres myapp"

RUN pip install --upgrade pip  --no-cache-dir
RUN pip install "poetry"
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

CMD uvicorn $UVICORN_ARGS
