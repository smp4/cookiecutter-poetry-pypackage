---
title: Development 
summary: How to develop {{ cookiecutter.project_name }}. 
authors:
    - {{ cookiecutter.full_name }} 
date: {% now 'local', '%Y-%m-%d' %}
---


## Installing from source for development

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

## Installing from a local build

```shell
$ make dist
```

If your package should be run as a command-line application, the recommended method is to use `pipx` so that your software and its dependencies are installed into its own isolated environment, without polluting your python interpreter's `site-packages`. This can be done with:

```bash
$ pipx install dist/<<package_name_with_version>>.tar.gz
```

or 

```bash
$ pipx install dist/<<package_name_with_version>>.whl
```


## Boilerplate

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

