FROM python:3.15-alpine@sha256:0f9552bb28711333da16915ec146f5e6bb44a7fdac9ced15dc17c2e0206346dd

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest@sha256:a3ea1357342c1a4bf9a0c53a3deb1b55379aefa037338d8113d5771efa01774f /uv /usr/local/bin/uv

WORKDIR /shreddit

# Copy project files
COPY pyproject.toml README.md ./
COPY shreddit ./shreddit

# Install the project with uv
RUN uv pip install --system --no-cache .

VOLUME /config
WORKDIR /config

CMD ["/usr/local/bin/shreddit"]
