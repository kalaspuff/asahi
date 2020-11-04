SHELL := /bin/bash
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
	cp asahi/__version__.py asahi/extras/__version__.py
	if cp pyproject.toml asahi-backup.toml && \
			poetry version `python asahi/__version__.py` && \
			cp pyproject.toml asahi.toml && \
			cp asahi-extras.toml pyproject.toml && \
			poetry version `python asahi/__version__.py`; then \
		cp pyproject.toml asahi-extras.toml ; \
		mv asahi.toml pyproject.toml ; \
		rm asahi-backup.toml ; \
	else \
		mv asahi-backup.toml pyproject.toml ; \
		rm asahi.toml ; \
	fi

black:
	poetry run black asahi/ tests/

isort:
	poetry run isort asahi/ tests/

build:
	rm -rf dist/

	cp asahi/__version__.py asahi/extras/__version__.py
	if cp pyproject.toml asahi-backup.toml && \
			poetry build && \
			cp pyproject.toml asahi.toml && \
			cp asahi-extras.toml pyproject.toml && \
			poetry build; then \
		cp pyproject.toml asahi-extras.toml ; \
		mv asahi.toml pyproject.toml ; \
		rm asahi-backup.toml ; \
	else \
		mv asahi-backup.toml pyproject.toml ; \
		rm asahi.toml ; \
	fi

.PHONY: _pypi_release
_pypi_release:

release:
	make pytest
	make flake8
	make mypy
	make version
	make build

	poetry run twine upload dist/asahi-extras-`python asahi/__version__.py`* dist/asahi_extras-`python asahi/__version__.py`*
	poetry run twine upload dist/asahi-`python asahi/__version__.py`*

	poetry lock
	git add pyproject.toml poetry.lock asahi-extras.toml asahi/__version__.py asahi/extras/__version__.py

	git commit -m "Bumped version to `python asahi/__version__.py`" --allow-empty
	git tag -a `python asahi/__version__.py` -m `python asahi/__version__.py`
	git push
	git push --tags

test: pytest flake8 mypy
tests: test
dist: build
lint: flake8 mypy
pylint: flake8 mypy
