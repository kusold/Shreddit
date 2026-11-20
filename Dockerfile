FROM python:3.15-alpine@sha256:0f9552bb28711333da16915ec146f5e6bb44a7fdac9ced15dc17c2e0206346dd

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest@sha256:d3b601f0c7b118bc1753febf7c41cc80981df678445e0254284eecf84db79a7d /uv /usr/local/bin/uv

WORKDIR /shreddit

# Copy project files
COPY pyproject.toml README.md ./
COPY shreddit ./shreddit

# Install the project with uv
RUN uv pip install --system --no-cache .

VOLUME /config
WORKDIR /config

CMD ["/usr/local/bin/shreddit"]
