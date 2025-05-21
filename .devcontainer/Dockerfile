# Start from the official Python devcontainer base image
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    libgirepository1.0-dev \
    pkg-config \
    python3-dev \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry (official method)
# Install Poetry for the vscode user
USER vscode

ENV POETRY_VERSION=2.1.3
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.profile

# Add Poetry to PATH immediately (for non-login shells)
ENV PATH="/home/vscode/.local/bin:$PATH"

# Optional: Set Poetry to not create virtual environments inside the container
RUN /home/vscode/.local/bin/poetry config virtualenvs.in-project true

# Switch back to root if needed for later setup
USER root