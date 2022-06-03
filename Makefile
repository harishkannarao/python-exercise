init:
	pip install pipenv --upgrade
	pipenv install --dev

update:
	pipenv update

test:
	pipenv run python -m pytest --html=report.html --self-contained-html

flake8:
	pipenv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length

requirements:
	pipenv requirements > requirements.txt

requirements_with_dev:
	pipenv requirements --dev > requirements.txt