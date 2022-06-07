# python exercise

Repository to explore python programming, testing and bundling of python programs

## Tools Required

* python `3.9`
* make `3.81`
* git `latest`
* pycharm `latest`

## Commands

### Install dependencies

    make init

### Update packages to latest

    make update
    
### Run tests

    make test
    
### Verify flake8

    make flake8
    
### Create requirements.txt

    make requirements 

### Create requirements.txt including dev packages

    make requirements_with_dev

### Install dependencies from requirements.txt during runtime

    pip install -r requirements.txt
    
### Create distribution

    make clean init requirements create_distribution