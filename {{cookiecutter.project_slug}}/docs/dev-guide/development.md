---
title: Development 
summary: How to develop {{ cookiecutter.project_name }}. 
authors:
    - {{ cookiecutter.full_name }} 
date: {% now 'local', '%Y-%m-%d' %}
---

Clone the repo:

```shell
$ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
```

`Poetry` is required. Optionally set a local python version with `pyenv`.

```shell
$ pipx install poetry
$ poetry install
$ poetry info
```

Run {{cookiecutter.project_name}} from source tree on your machine:

```shell
$ poetry run python -m {{cookiecutter.project_slug}}
```

Keeping the boilerplate up to date with the original [cookiecutter template](https://github.com/smp4/cookiecutter-poetry-pypackage):

```shell
$ pipx install cruft
$ cruft check
$ cruft update
```

Run the checks and tests:

``` shell
$ make checks
$ make test
```

