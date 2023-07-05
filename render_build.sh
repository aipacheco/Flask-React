#!/usr/bin/env bash
# exit on error
set -o errexit
pipenv install
pipenv run upgrade
npm install
npm run build
