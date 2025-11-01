FROM python:3.11.0-alpine

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /shreddit

# Copy project files
COPY pyproject.toml ./
COPY shreddit ./shreddit

# Install the project with uv
RUN uv pip install --system .

VOLUME /config
WORKDIR /config

CMD ["/usr/local/bin/shreddit"]
