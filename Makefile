.PHONY: test version tests build dist release
ifndef VERBOSE
.SILENT:
endif

default:
	@echo "Usage:"
	@echo "- make test         | run tests"
	@echo "- make black        | run black -l 120"
	@echo "- make release      | upload dist and push tag"

pytest:
	PYTHONPATH=. poetry run pytest --cov-report term-missing --cov=asahi tests/

flake8:
	poetry run flake8 asahi/ tests/

mypy:
	poetry run mypy asahi/

version:
	poetry version `python asahi/__version__.py`

black:
	poetry run black asahi/ tests/

isort:
	poetry run isort asahi/ tests/

build:
	rm -rf dist/
	poetry build

release:
	make pytest
	make flake8
	make mypy
	make version
	make build
	poetry publish
	git add pyproject.toml asahi/__version__.py
	git commit -m "Bumped version" --allow-empty
	git tag -a `python asahi/__version__.py` -m `python asahi/__version__.py`
	git push
	git push --tags

test: pytest flake8 mypy
tests: test
dist: build
lint: flake8 mypy
pylint: flake8 mypy
