# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

FROM python:3.8-slim-buster AS venv
LABEL maintainer=pipinfitriadi@gmail.com
RUN --mount=type=cache,target=/var/cache/apt \
    apt update && \
    apt install -y \
        git \
        # For Python Lib: mysqlclient
        gcc \
        default-libmysqlclient-dev \
        pkg-config
RUN pip install \
        --root-user-action=ignore \
        --no-cache-dir \
        --upgrade \
        pip && \
    pip install \
        --root-user-action=ignore \
        --no-cache-dir \
        toml
# Download dependencies declared in pyproject.toml using pip #11927
# https://github.com/pypa/pip/issues/11927#issuecomment-1498795083
COPY pyproject.toml /tmp/pyproject.toml
RUN python \
        -c 'import toml; c = toml.load("/tmp/pyproject.toml"); print("\n".join([*c["project"].get("dependencies", []), *[row for optional_dependency in c["project"].get("optional-dependencies", {}).values() for row in optional_dependency]]))' \
        > /tmp/requirements.txt && \
    pip install \
        --root-user-action=ignore \
        --no-cache-dir \
        --target=/opt/venv/ \
        -r /tmp/requirements.txt
COPY . /repo/
RUN pip install \
        --root-user-action=ignore \
        --no-cache-dir \
        --target=/opt/venv/ \
        --upgrade \
        git+file:/repo/

FROM python:3.8-slim-buster AS app
LABEL maintainer=pipinfitriadi@gmail.com
ENV PYTHONPATH $PYTHONPATH:/opt/venv/
ENTRYPOINT ["/opt/venv/bin/datasae"]
CMD ["--help"]
COPY --from=venv /opt/venv/ /opt/venv/
