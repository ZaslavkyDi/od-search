install_poetry:
	poetry run scripts/install_poetry.sh

start:
	python app/main.py


pytest-cover:
	poetry run pytest --cov=app tests/
