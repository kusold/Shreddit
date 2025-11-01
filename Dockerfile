FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /shreddit

# Copy project files
COPY pyproject.toml ./
COPY shreddit ./shreddit

# Install the project with uv
RUN uv pip install --system --no-cache .

VOLUME /config
WORKDIR /config

CMD ["/usr/local/bin/shreddit"]
