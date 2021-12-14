SCRPATH := $(CURDIR)

define HELP

This is aoc's Makefile.

Usage:

	setup - Setup the project.
	test - Run the tests.
	check-format - Check if black and isort formats pass.
	format - format the project using black and isort.

endef

export HELP

.PHONY: all help setup setup-ci run test check-format format

all help:
	@echo "$$HELP"

setup:
	poetry install

setup-ci:
	poetry install --no-interaction

test:
	poetry run pytest -n 2 --cov

check-format:
	poetry run isort -c $(SCRPATH)
	poetry run black --check $(SCRPATH)

format:
	poetry run isort $(SCRPATH)
	poetry run black $(SCRPATH)
