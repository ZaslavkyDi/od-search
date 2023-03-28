# https://github.com/michael0liver/python-poetry-docker-example/blob/f7241bf6586e99c6c649eba36ca0efd935ea6316/docker/Dockerfile

FROM python:3.11.0-slim as python-base
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# builder-base is used to build dependencies
FROM python-base as builder-base
RUN apt-get -y update; apt-get -y install curl
RUN pip install poetry

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-dev

# 'release' stage uses the clean 'python-base' stage and copies
# in only our runtime deps that were installed in the 'builder-base'
FROM python-base as release
ENV FASTAPI_ENV=production

RUN adduser --disabled-login appuser
COPY --from=builder-base --chown=appuser $VENV_PATH $VENV_PATH

USER appuser
WORKDIR /home/appuser

# Copy in scripts and supporting configuration files
COPY --chown=appuser scripts scripts
RUN chmod +x scripts/*
COPY --chown=appuser pyproject.toml .

COPY --chown=appuser od_search od_search

EXPOSE 8880
ENTRYPOINT ["/home/appuser/scripts/docker-entrypoint.sh"]
CMD scripts/start.sh
