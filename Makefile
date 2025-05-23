# Makefile for harmony-tools project

PYTHON=python3
POETRY=poetry
PROJECT_NAME=harmony-tools

.PHONY: help install dev clean lint test export-requirements

help:
	@echo "Usage:"
	@echo "  make install               Install dependencies"
	@echo "  make clean                 Remove __pycache__ and build artifacts"
	@echo "  make lint                  Run flake8 linting"
	@echo "  make format				Run blck formatting"
	@echo "  make test                  Run tests"
	@echo "  make requirements			Export requirements.txt"

install:
	$(POETRY) install

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf dist *.egg-info .pytest_cache .mypy_cache

lint:
	$(POETRY) run flake8 src tests

format:
	$(POETRY) run black src tests

test:
	PYTHONPATH=src $(POETRY) run pytest

requirements:
	$(POETRY) export -f requirements.txt --output requirements.txt --without-hashes