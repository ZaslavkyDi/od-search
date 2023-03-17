install_poetry:
	poetry run scripts/install_poetry.sh

install_pre_commit:
	poetry run scripts/install_pre_commit.sh

start:
	python app/main.py

pytest-cover:
	poetry run pytest --cov=app tests/

ruff:
	ruff . --fix

black:
	black .
