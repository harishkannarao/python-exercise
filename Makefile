init:
	pipenv install --dev

test:
	pipenv run python -m unittest discover -s tests -p "*_test.py"

flake8:
	pipenv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length

requirements:
	pipenv lock -r > requirements.txt