FROM python:3.12-slim as build

ENV PYTHONUNBUFFERED 1 \
    PIP_DISABLE_VERSION_CHECK 1 \
    PIP_NO_CACHE_DIR 1 \
    DEBIAN_FRONTEND=noninteractive

RUN set -ex \
    && addgroup --gid 50000 python \
    && adduser --shell /bin/false --disabled-password --uid 50000 --gid 50000 --no-create-home python \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./pkg/requirements.txt
RUN pip install -r ./pkg/requirements.txt

FROM build as base

WORKDIR "/app"

COPY ["pyproject.toml", "requirements.txt", "./pkg/"]

COPY mdiscord ./pkg/mdiscord
RUN python -m pip install ./pkg \
    && rm -rf ./pkg

USER python
