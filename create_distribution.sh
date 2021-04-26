#!/bin/sh

rm -rf python-exercise.zip requirements.txt

make init test flake8 requirements

FILE_NAME=python-exercise.zip

zip $FILE_NAME \
    requirements.txt \
    main.py

zip -r $FILE_NAME my_module/*