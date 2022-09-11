# Shamelessly taken from https://github.com/drivendata/cookiecutter-data-science
# and https://github.com/audreyfeldroy/cookiecutter-pypackage

.PHONY: dev-install clean clean-build clean-pyc clean-test test test-all dist docs help checks release

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.project_slug }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install the required python interpreter and project dependencies into editable mode
dev_install: pyproject.toml
	pyenv install {{ cookiecutter.python_version }}
	pyenv local {{ cookiecutter.python_version }}
	pipx install poetry
	poetry install
	poetry info


## Delete all compiled Python files, build, test and coverage artifacts
clean: clean-build clean-pyc clean-test

## remove build artifacts
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

## Remove Python file artifacts
clean-pyc:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
#	find . -name '*.pyc' -exec rm -f {} +
#	find . -name '*.pyo' -exec rm -f {} +
#	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*~' -exec rm -f {} +

## Remove test and coverage artifacts
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

## Autoformatters should run first, then style check to verify autoformtters. Then type checks and linters.

## Check format with black
{%- if cookiecutter.use_black == 'y' %}
.PHONY: checks-black
checks-black:
	poetry run black --check src tests
{%- endif %}

## Auto-sort imports
{%- if cookiecutter.use_isort == 'y' %}
.PHONY: checks-isort
checks-isort:
	poetry run isort src tests
{%- endif %}

## Auto-update docstrings with docformatter
{%- if cookiecutter.use_docformatter == 'y' %}
.PHONY: checks-docformatter
checks-docformatter:
	poetry run docformatter src tests
{%- endif %}

## Check type hinting with mypy
{%- if cookiecutter.use_black == 'y' %}
.PHONY: checks-mypy
checks-mypy:
	poetry run mypy --strict src tests
{%- endif %}

## Check style with pylint
{%- if cookiecutter.use_pylint == 'y' %}
.PHONY: checks-pylint
checks-pylint:
	poetry run pylint src tests
{%- endif %}

## Check style with yamllint
{%- if cookiecutter.use_yamllint == 'y' %}
.PHONY: checks-yamllint
checks-yamllint:
	poetry run yamllint . -c yamllint-config.yml
{%- endif %}

## Check style with flake8
{%- if cookiecutter.use_flake8 == 'y' %}
.PHONY: checks-flake8
checks-flake8:
	poetry run flake8 src tests
{%- endif %}

## Check code security with bandit
{%- if cookiecutter.use_bandit == 'y' %}
.PHONY: checks-bandit
checks-bandit:
	poetry run bandit -r .
{%- endif %}

## Code quality checks
checks: {%- if cookiecutter.use_black == 'y' %}checks-black{%- endif %} {%- if cookiecutter.use_isort == 'y' %}checks-isort{%- endif %} {%- if cookiecutter.use_docformatter == 'y' %}checks-docformatter{%- endif %} {%- if cookiecutter.use_mypy == 'y' %}checks-mypy{%- endif %} {%- if cookiecutter.use_pylint == 'y' %}checks-pylint{%- endif %}	{%- if cookiecutter.use_yamllint == 'y' %}checks-yamllint{%- endif %}	{%- if cookiecutter.use_flake8 == 'y' %}checks-flake8{%- endif %}	{%- if cookiecutter.use_bandit == 'y' %}checks-bandit{%- endif %}

### Run tests quickly. Extra params in pyproject.toml.
test:
{%- if cookiecutter.use_pytest == 'y' %}
	poetry run pytest tests
{%- else %}
	@echo ">>> pytest not installed. Testing not possible!"
{%- endif %}

## Run tests on every Python version with tox
test-all:
	@echo ">>> Tox not implemented yet!"

## Generate local Mkdocs-Material html documentation, including API docs.
docs:
	poetry run mkdocs serve
## $(BROWSER) docs/_build/html/index.html

{%- if cookiecutter.use_pypi == 'y' %}
## Publish to PyPI
release: dist
	poetry publish {{ cookiecutter.project_slug }}
{%- endif %}

## Builds source and wheel package with Poetry
dist: clean
	poetry build


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################
# Other tools for managing DAGs that are written in Python instead of a DSL:
# Paver, Luigi, Airflow, Snakemake, Ruffus, or Joblib.....

{%- if cookiecutter.use_datascience == 'y' %}
## Template for using the Makefile in analysis (analysis as a DAG)
data: dev_install
	poetry run make_dataset.py data/raw data/processed
{%- endif %}

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
