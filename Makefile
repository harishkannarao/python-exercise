init:
	pipenv install --dev

test:
	pipenv run python -m pytest --html=report.html --self-contained-html

flake8:
	pipenv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length

requirements:
	pipenv lock -r > requirements.txt