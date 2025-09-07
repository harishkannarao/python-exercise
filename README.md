# python exercise

Repository to explore python programming, testing and bundling of python programs

## Tools Required

* python `>=3.11`
* make `3.81`
* git `latest`
* pycharm `latest`

## One Time PyCharm Setup

Setup `python` interpreter to virtual env as:

    Settings -> Project: <Project Name> -> Python Interpreter -> Add Interpreter -> Add Local Interpreter -> Select Existing -> Python -> <Project Root>/.venv/bin/python

To run `pytest` tests in `PyCharm`, make the project root directory as test root directory by

    Right Click Project Root directory -> Mark Directory As -> Test Sources Root

## Commands

### Install dependencies

    make init

### Update packages to latest

    make upgrade
    
### Run tests

    make test
    
### Verify flake8

    make flake8

### Run main.py

    uv run main.py

### Run full build

    make run_all
    
### Create requirements.txt

    make requirements 

### Create requirements.txt including dev packages

    make requirements_with_dev

### Install dependencies from requirements.txt during runtime

    pip install -r requirements.txt
    
### Create distribution

    make clean init requirements create_distribution