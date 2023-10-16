.DEFAULT_GOAL := run_all

init:
	pip install pipenv --upgrade
	pipenv install --dev

clean:
	pipenv run python clean.py

update:
	pipenv update

test:
	pipenv run python -m pytest --html=report.html --self-contained-html

flake8:
	pipenv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length

run_all:
	make clean init test flake8

requirements:
	pipenv requirements > requirements.txt

requirements_with_dev:
	pipenv requirements --dev > requirements.txt

create_distribution:
	pipenv run python create_distribution.py