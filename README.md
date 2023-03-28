## Table Of Content
- [Overview](#overview)
- [How To Install](#how-to-install)
- [How To Run](#how-to-run)
- [How To Reach The API docs](#how-to-reach-the-api-docs)
- [Link To DockerHub Repository](#link-to-dockerhub-repository)


### Overview

This is a small Web App will save your time for filtering Orderful Dashboard transactions by their content and regular filter such as:

- Direction
- Transaction Type
- Business Number
- Transaction Content


### How To Install

- Be sure that you are using Python 3.11 or higher.
- Activate virtual environment with commands:
    - <code> python3 -m venv venv </code>
    - <code> source venv/bin/activate </code>


- Install poetry and project dependencies with a command:
    - <code> make install_poetry </code>


- Install pre-commit [Optional]:
    - <code> make install_pre_commit </code>

### How To Run
- Run from _main.py_ file:
  - <code> python od_search/main.py </code>


- Run from _Makefile_ file:
  - <code> make start </code>


### How to reach the API docs
By default the app is up on port <code>8880</code> to reach the API docs use one of the next links:

- ReDoc: http://localhost:8880/redoc
- Swagger: http://localhost:8880/docs
- Openapi: http://localhost:8880/openapi.json


### [Link To DockerHub Repository](https://hub.docker.com/repository/docker/zaslavskyd/od-search/general)
