install_poetry:
	poetry run scripts/install_poetry.sh

install_pre_commit:
	poetry run scripts/install_pre_commit.sh

start:
	python app/main.py

pytest-cover:
	poetry run pytest --cov=app tests/

ruff:
	poetry run ruff . --fix

black:
	poetry run black .


# Docker
docker-build:
	poetry run scripts/docker-build.sh $(tag)

docker-publish:
	poetry run scripts/docker-build.sh $(tag)
	poetry run scripts/docker-publish.sh $(tag)
	poetry run scripts/docker-clean.sh $(tag)

docker-clean:
	poetry run scripts/docker-clean.sh $(tag)

docker-run:
