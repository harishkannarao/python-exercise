.DEFAULT_GOAL := run_all

init:
	uv sync --locked

init_ci:
	pip install uv --upgrade
	uv sync --locked

clean:
	uv run python clean.py

upgrade:
	uv sync --upgrade

test:
	uv run python -m pytest --html=report.html --self-contained-html

ruff:
	uv run ruff check
	uv run ruff format

flake8:
	uv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length

run_all:
	make clean init test ruff flake8

requirements:
	uv export --no-dev --format requirements-txt > requirements.txt

requirements_with_dev:
	uv export --all-groups --format requirements-txt > requirements.txt

create_distribution:
	uv run python create_distribution.py