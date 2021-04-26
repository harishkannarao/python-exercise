#!/bin/sh

rm -rf python-exercise.zip requirements.txt

make init test flake8 requirements

zip python-exercise.zip \
    requirements.txt \
    main.py

zip -r python-exercise.zip my_module/*