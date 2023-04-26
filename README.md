# Cookiecutter-Poetry-Pypackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package using Poetry, MkDocs-Material and (optional) layout for data processing.

This template is a work in progress. Please create an issue if you find something that doesn't work!

## Features

Main features include:
  - [`cruft`](https://cruft.github.io/cruft/) to keep you up to date with this template. 
  - [`Poetry`](https://github.com/python-poetry/poetry): Dependency management and packaging.
  - [`pytest`](https://github.com/pytest-dev/pytest): Unit and coverage testing.
  - [`flake8`](https://github.com/PyCQA/flake8) and [`pylint`](https://github.com/PyCQA/pylint): Python style checks, with a bunch of plugins, including `tryceratops`.
  - [`black`](https://github.com/psf/black): Auto-formatted code.
  - [`docformatter`](https://docformatter.readthedocs.io/en/latest/index.html): Autoformat your docstrings (defaults to Google style).
  - [`isort`](https://pycqa.github.io/isort/): Sort your imports.
  - [`mypy`](https://github.com/python/mypy): Type checking.
  - [`Bandit`](https://github.com/PyCQA/bandit): Find common security issues.
  - [`MkDocs-Material`](https://github.com/squidfunk/mkdocs-material): Auto-publish documentation to it's own web page.
  - [`mkdocstrings-python`](https://github.com/mkdocstrings/python): Wrapping [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings) for automatic API documentation from sources.
  - [`GitHub Actions`](https://github.com/features/actions): Automated CI checks, auto-release to PyPi, with automated automated version bumping when publishing.
  - [`ipykernel`](https://github.com/ipython/ipykernel): (Optional) Tooling set up for use of virtual environment as kernel in [Jupyter](https://jupyter.org/) notebooks, creates convenience directories, and a template `*.ipynb`.
  - [`logging`](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial): Set up out of the box for library and app usage. See *Opinions* for more. Only uses default Python `logging` library.
  - [`click`](https://palletsprojects.com/p/click/) and `Argparse`: (Optional) CLI for your app.
  - `src` layout: See [why](https://py-pkgs.org/04-package-structure.html#the-source-layout).
  - Template for new Python source files.
  - Makefile: So you don't have to remember commands.

## Opinions

* Develop as a package.
* As much project configuration in `pyproject.toml` as possible. Unfortunately not possible for `flake8`.
* `logging` is set up according to [Twelve Factor App](https://12factor.net/logs) principles. The library logs to the `NullHandler` unless the calling application implements its own application-specific handlers. A default configuration is applied if the package is called with `python -m {{cookiecutter.project_slug}}`, sending logs as streams to `stdout` and `stderr` for the application user to route and store as necessary. Logs are coloured for easy reading on the console, and stack traces are converted to single line entries. Modify `logsetup.py`to change this behaviour.
* All documentation and docstrings in `Markdown`. No ReStructured text. Use a single syntax everywhere. 
* The structure of the documentation takes the [MkDocs Documentation](https://www.mkdocs.org/) as inpsiration. No symlinks are used between docs in `docs/` and source code files like `CONTRIBUTING` and `CHANGELOG`. Instead, this two files are taken out of source code and put in the `docs/` tree so that `MkDocs` can link to them when statically and dynamically linked, and to avoid duplicating information in the project.

## Assumptions

The following tools are already assumed to be installed: `poetry`, `pipx`, `pyenv`, `jupyter-lab`.

## Options

* `full_name` Your full name as you wish the world to see it.
* `email` Public facing contact email address.
* `github_username` Your GitHub account username. Required for GH integrations. Credentials not requested.
* `project_name` Full name of the project. Can include spaces, capitals etc.
* `project_slug` underscore, no-spaces version of the project name. Should be the same as the GitHub repo name. Normally just use the default.
* `project_short_description` A one-liner that appears in headers and other short description fields.
* `python_version` Version of Python that the package shall run against. Used to set up the virtual environment with `poetry` and `pyenv`. **Must** be a full version specification eg. 3.10.6, or else you will get errors when using `poetry` and `pyenv`.
* `open_source_license` Select an open source license. See [choosealicense](https://choosealicense.com/).
* `create_author_file` Create an `AUTHOR.md` file or not.
* `use_xxx` Use `xxx` package or not.
* `use_jupyter` Adds `notebooks` and `reports` directories. Installs an IPython kernel from the project env available to Jupyter in Jupyter's env. Assumes `Jupyter Lab` is already installed and available.
* `command_line_interface` Choose a package to set up a boilerplate CLI (or none).
* `use_pypi` Set up GitHub Actions for CI/CD to PyPI.
* `pypi_username` PyPI username. Only used if `use_pypi` is selected.
* `use_github_actions_for_pypi_deployment` As the name suggests. Sets up hooks for GH actions.
* `use_github_actions_for_ci` As the name suggests. Sets up GH actions for code checks and testing.
* `use_github_actions_to_publish_docs` Sets up GH action to publish docs to GH with `MkDocs`.
* `use_datascience` Sets up data and models  directories.


## Template Installation

This section describes how to install the template and run a first setup for your project. See the `README.md` in the template for how users should install your package/ application.

### Bake the Cookie
This guide assumes `pyenv`, `pipx` and `poetry` are installed. Only `poetry` is mandatory for this package to work. The Makefile will probably throw errors if `pyenv` and `pipx` are not installed.

Install the latest Cookiecutter if you haven't installed it yet (`Cookiecutter 1.4.0` or higher is required):

```shell
$ pipx install cookiecutter 
$ cookiecutter --version
```

`cd` into the directory that houses all of your projects. Bake the new project from the template and make your selections, see *Options* to see what effect your choices will have. 

```shell
$ cookiecutter https://github.com/smp4/cookiecutter-poetry-pypackage.git
```

#### Optional: Baking with Cruft
`Cruft` helps you keep your project boilerplate up to date by syncing your project with updates to the originating cookiecutter template repository. It uses `cookiecutter` templates just the same as `cookecutter`.

`Cruft` is not in the project dev dependencies, since it is optional. Instead, install it to your system with `pipx`, then bake the cookie:

```shell
$ pipx install cruft
$ cruft create https://github.com/smp4/cookiecutter-poetry-pypackage.git
```

A default `Cruft` configuration is in `pyproject.toml` just in case you want to use it.

At any time in your project development, you can check to see if your boilerplate is up to date with the latest template. In the root of the project, run:

```shell
$ cruft check
$ cruft update
```


### Remote Git Repo Initialisation
Create the remote repository on GitHub [creating a new repository](https://github.com/new) on GitHub. Leave all boxes unchecked in the *New Repository* dialogue. 

The GitHub repository name should be the same as the `cookiecutter.project_slug` which will be the name of the project, but with all letters lower case and spaces and hyphens converted to underscores.

### Local Git Repo Initialisation

`cd` into the directory that cookiecutter just made for your new project. 

Set up the local git repository in your project directory and rename the default branch to `main` for GitHub compatibility:

```shell
$ git init
$ git add .
$ git commit -m "repo initialisation"
$ git branch -m master main  # Rename master branch to main, for GH compatibility
$ git status  # Should state "On branch main"
$ git remote add origin git@github.com:<<github_username>>/<<repo_name>>.git
$ git push -u origin main
```

### Initialise the Project
Optionally, set up a local python version with `pyenv`. Remember which version of python you specified when you baked the cookie! For example -

```shell
pyenv install 3:latest  # 3.10.6
pyenv local 3.10.6
```

**Note!** By default, Poetry uses the Python version used during Poetry installation to create new virtual environments. Using the above workflow with `pyenv`, this means that Poetry would normally ignore the local python version set by `pyenv local 3.10.6`. This cookiecutter template avoids this by setting `virtualenvs.prefer-active-python = true` in `poetry.toml`. See [more here](https://python-poetry.org/docs/configuration/#virtualenvsprefer-active-python-experimental).

Now initialise everything with the makefile. This will install the template project with `poetry` and run a first check of all the code.

```shell
$ make dev_install
$ make clean  
$ make checks
```

If you would rather do all this manually, look at the `Makefile` and copy the commands out into the terminal one by one yourself. 

To check that the environment was installed as expected:

```shell
$ poetry env list
$ poetry env info
$ poetry show --tree
```

### Add the Virtual Environment to Jupyter-Lab Kernel List

If you want to use `Jupyter-Lab` as part of your project development flow, it can be useful to add the virtual environment of your project other `Jupyter-Lab` kernel list. This allows you to select the virtual environment of your project in the kernel list in your notebooks.

For this to work, you should have selected the `use_jupyter` option in the cookiecutter setup to install `ipykernel`.

From within your projects root directory run the following:

```shell
$ poetry run python -m ipykernel install --prefix=/path/to/jupyter/env --name <<venv_name>> --display-name "Python (<<venv_name>>)"
```

where `/path/to/jupyter/env` is the path to the virtual environment where Jupyter has been installed (and therefore where the kernel will be installed). It could be `/home/<<user>>/.local/pipx/venvs/jupyterlab` if Jupyter is installed with `pipx`, for example.

The `<<venv_name>>` should be replaced with the text used for `project_slug` in the cookiecutter template: this is the name of your virtual environment.

### More GitHub Setup

#### Set up Branches
Create development branch:

1. Click on the "main" dropdown button your repo's homepage.
2. Type in "develop" in the search bar.
3. Select "Create branch: develop from main". 

Alternatively, from the command line:

```shell
$ git checkout -b develop main
$ git push -u origin develop
```

If GitHub workflows are enabled, opening a pull request from `develop` to `main` will automatically run code checks to make sure it is safe to merge. 

#### Set up Documentation page on GitHub

Requires a public repository or an upgraded GitHub account.

Github Actions will have created a `gh-pages` branch. All the files in that branch are automatically generated from the files in the repository's docs folder. For more information on how to add pages to this documentation visit [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) docs.

GitHub repositories automatically serve static content when committed to a branch named `gh-pages`.

To publish the docs to your own github site do the following:

1. Go to "Settings" section.
2. Scroll down to "Pages" section.
3. Within the "Source" section select `gh-pages` branch and `/(root)`.
4. Click "Save" button.

Scroll back down to "GitHub Pages" and a link should be given for where your docs will be published (wait a few minutes for publication). In addition, this link can be added in the About section of your repository under "website" to display the link in a nice area.


## Development Flow

Develop on the development branch. Only push to main for publication of stable, checked, tested production-ready code.

The cookiecutter creates a project which has a release action for release candidates ("prereleased") and a separate one for production releases. The logic for why is as follows:

* Before merging into main (and releasing to production) the developer should develop the code on the development branch. 
* With the development code thought to be ready for production, the developer would create a release candidate (otherwise known as pre-release) which ships the package to test pypi. 

This is done so the package can be downloaded and user-tested without messing up the release history of your pypi package. In addition, it's typically recommended to only have production-ready code on your main branch.

### Git Commit Tags for Changelog Generation

Use tags in git commits: added `add`, change `chg`, deprecated `dep`, removed `rem`, fixed `fix`, security `sec`.

### Developing the Documentation

Documentation is also stored in the development branch, in sync with the development code. If GitHub actions are enabled, then the documentation hosted on GitHub will be published for public use only when the `main` branch is updated. 

While on the development branch, use the locally generated site (`poetry run mkdocs serve`) to check your documentation as you develop it.

### Scripts

To run the package as a script before installing, because the `__main__.py` is present in `src` directory, you can to run the module as a script using `poetry run python -m your_package`.

If you add scripts to the project, add them to the `pyproject.toml` file and
run `poetry install` to make them available in the project's virtualenv. See
[`Poetry` docs](https://python-poetry.org/docs/pyproject/#scripts).

### Create Release Candidate and Publish to Test PyPI

These are the steps needed to publish to test PyPI from GitHub:

1. Navigate to the Releases section of your repository.
2. Click "Create a new release".
3. Set Tag version to 0.1.0-rc0.
4. Select development branch.
5. Set Release title to Release Candidate: v0.1.0 (or a fun name).
6. Select "This is a pre-release"
7. Click "Publish release"

Wait a few minutes (or watch the Github Action) for it to be published.

See [mgancita docs](https://mgancita.github.io/cookiecutter-pypackage/getting-started/publish_to_test_pypi/) for how to set up username/ password tokens/ secrets.

### Publishing to PyPI

See [mgancita docs](https://mgancita.github.io/cookiecutter-pypackage/getting-started/publish_to_pypi/).


### Installing from Source as a Command Line Application

Users can install your package from source. First, they clone and build the source:

```shell
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPO
$ make build  # Build source distribution (`*.tar.gz` in `your_package/dist`). Uses Poetry
```

If your package should be run as a command-line application, the recommended method is to use `pipx` so that your software and its dependencies are installed into its own isolated environment, without polluting your python interpreter's `site-packages`. This can be done with:

```bash
$ pipx install dist/your_package-1.0.tar.gz
```

or 

```bash
$ pipx install dist/your_package.whl
```

If using `pipx`, users can also install your software directly from GitHub source without having to package it to a source distribution (shown with ssh below). 

```bash
$ pipx install git+ssh://git@github.com:usr/package_name
```

If `pipx` is not available, then use `pip`, which will install it to `site-packages` of the current python interpreter:

```bash
$ python3 -m pip install dist/your_package-1.0.tar.gz
```

### Installing as a Library

This assumes you use `Poetry` to manage your environment and dependencies. Assuming that your package is on PyPI:

```bash
$ poetry add your_package
$ poetry install
```
 
For adding from other locations (GitHub repos, including with ssh, or local directories), see [`Poetry` docs](https://python-poetry.org/docs/cli/#add). 

Note, for a private GitHub repo, you may need to add `#main` to the end of the `add` line. `Poetry` defaults to using `master` otherwise:

```bash
$ poetry add git+ssh://git@github.com:usr/package_name.git#main
$ poetry install
```

See also adding dependencies for `Poetry` in the [`Poetry` docs](https://python-poetry.org/docs/dependency-specification/).

After the library is installed in the environment, you can use it in your code:

```python
# user_module.py
from your_project.your_file import YourClass
```

## Code Checks

The template sets up a number of code checks either via the makefile, or with GitHub actions if installed. 

The makefile only does checks, no changes are made. Instead, you should use the individual tools directly to do the autoformatting, for example:


```bash
$ poetry run black src tests
$ poetry run isort --profile="black" src tests 
$ poetry run docformatter --syntax="google" --recursive --black=True src tests
```

## Testing

```shell
$ make test
```

## Documentation

The template uses `MkDocs-Material` for documentation generated with Markdown files, and docstrings written in Markdown. For a tutorial on `mkdocs` see [RealPython](https://realpython.com/python-project-documentation-with-mkdocs/).

To set up navigation of your documentation, you need to put a page tree in the `mkdocs.yml` file. Note that each highest level list item becomes part of the top navigation menu. All nested items are shown within each section.

Following best practice, the documentation is already set up with different sections for: 

1. Tutorials: Learning oriented.
2. How-To Guides: Problem oriented.
3. Reference: Information oriented.
4. Explanation: Understanding oriented. 

### Docstrings

Google docstrings are recommended. The template is set up to generate an API reference for your package from Google-style docstrings using `mkdocstrings`. `mkdocstrings` can infer type hints, so there is no need to declare types in the docstrings.

Note also that `Mkdocstrings` allows you to insert docstring information directly into the markdown pages with the three colon `:::` syntax. 

Recommended way to create Google-style docstrings with type hints and Examples that can (optionally) be used by `doctest`:

```python
# calculations.py
from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)
```

Then

```bash 
(venv) $ python -m doctest calculator/calculations.py
```

Module docstrings should also be added to give a quick overview of the module, and list all functions that it exports with a one-line description of each.

### Building the Docs

To build your documentation and create the site/ directory that’ll contain all the necessary assets and static files that’ll allow you to host your documentation online, you can use the build command:

```shell
$ poetry run mkdocs build
```

This creates a `site/` directory.


### Serving the Docs

`Mkdocs` comes with a built-in development server that lets you preview the documentation locally as you work on it. Assuming you're in the same directory as `mkdocs.yml`:

```shell
$ mkdocs serve
```

or

```shell
$ make docs
```

Then go to [http://127.0.0.1:8000](http:/127.0.0.1:8000). `serve` will rebuild your documentation whenever anything in the configuration file, documentation directory, or theme directory changes.


## Versioning and Changelog
TODO


## Template Structure

```
├── AUTHORS.md        <- Authors list. 
│                        Requires create_author_file.
├── data              <- Data directories. Normally not synced to GitHub.
│   │                    Requires use_datascience.
│   ├── external      <- Data from third party sources.
│   ├── interim       <- Intermediate data that has been transformed.
│   ├── processed     <- The final, canonical data sets for modeling.
│   └── raw           <- The original, immutable data dump.
├── docs              <- Project documentation in raw markdown format. A MkDocs-Material project.
│   ├── about         <- About the project. CHANGELOG, CONTRIBUTING, license.
│   ├── api.md        <- API reference generated by docstrings in your source code.
│   ├── dev-guide     <- Advanced usage, detailed explanations and development guide.
│   │                    Not mandatory for basic usage.
│   ├── glossary.md   <- Glossary of terms used in the project and documentation.
│   ├── img           <- Image resource directory for the project docs.
│   ├── index.md      <- Starting page of the docs
│   ├── quickstart.md <- Instructions for a minimal startup with minimal reading.
│   └── user-guide    <- Detailed installation, step by step tutorials for new users, howtos for
│                        common tasks.
├── .editorconfig     <- See [editorconfig](https://editorconfig.org/).
├── .env_template     <- Template for a .env file. Will be renamed to .env after the template is
│                        baked.
├── .flake8           <- flake8 config file, since flake8 is not compatible with a pyproject.toml.
├── .github           <- Configuration files for GitHub actions.
│                     <- Requires use_github_actions_xx.
├── .gitignore        <- Default gitignore file
├── LICENSE           <- License file if open source.
│                        Requires a selection from the open_source_license option.
├── Makefile          <- Makefile with common setup commands. Use this for any data manipulation.
│                        [Analysis = DAG](https://drivendata.github.io/cookiecutter-data-science/).
├── mkdocs.yml        <- Configuration file for mkdocs.
├── models            <- Trained and serialized models, model predictions, or model summaries.
│                        Requires use_datascience.
├── notebooks         <- Jupyter-Lab notebooks directory.
│   │                    Naming convention is a number (for ordering), the creator's initials, 
│   │                    and a short `-` delimited description, e.g. 
│   │                    `1.0-jqp-initial-data-exploration`. 
│   │                    Refactor the good parts into the package!
│   │                    Requires use_jupyter. 
│   ├── exploratory   <- For exploration. Includes a template notebook.
│   └── reports       <- For communication.
├── poetry.toml       <- Poetry configuration file.
├── pyproject.toml    <- Poetry/ python configuration file for the project.
├── pysource_template.py <- Template file with boilerplate and reminders for new python source 
│                        files.
├── README.md         <- README file.
├── references        <- Data dictionaries, manuals, and all other explanatory materials.
│                        Requires use_datascience.
├── reports           <- Generated analysis as HTML, PDF, LaTeX, etc.
│                        Requries use_jupyter.
│   └── fig           <- Generated graphics and figures to be used in reporting.
├── src               <- Source code tree for the project.
│   └── {{cookiecutter.project_slug}}
│       ├── __init__.py <- Makes the directory a Python module.
│       ├── __main__.py <- Main script for command line entry point. 
│       ├── cli.py    <- Command line module.
│       │                Requires a selection from command_line_interface option.
│       ├── logsetup.py <- Boilerplate for setting up logging as a package and application.
│       ├── py.typed    <- Declares the package to be a PEP 561 compliant stub package.
│       └── resources   <- Package configuraiton data etc to be loaded to make the package work.
│                          Not for large data files. Provide scripts to download this from
│                          elsewhere.
├── tests               <- Tests to be run with pytest.
│   ├── __init__.py
│   └── test_{{cookiecutter.project_slug}}.py
│                       <- Template for tests, with boilerplate code.
└── yamllint-config.yml <- yamllint configuration file.
```

## Maintaining this Cookiecutter template

```shell
$ poetry install
$ poetry run black .
$ poetry run flake8 \{\{cookiecutter.project_slug\}\}
```

## Security

Before installing unknown packages, review them at:

* https://snyk.io/advisor/
* https://osv.dev/

## Future Work

* Optional Terminal User Interface (TUI)
* Automatic version bumping, [Semantic Versioning](https://semver.org/), development cycle and changelog (see [keepachangelog](https://keepachangelog.com/en/1.0.0/)):
    * Possible tool - [gitchangelog](https://github.com/vaab/gitchangelog#incremental-changelog#)
    * Mimic [Python Development Guide](https://devguide.python.org/developer-workflow/development-cycle/#devcycle).
    * https://python-semantic-release.readthedocs.io/en/latest/
    * [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/
* implement features to protect against supply chain attacks: import typos
* badges, https://pylint.pycqa.org/en/latest/user_guide/installation/badge.html
* set up pre commit hooks.
    * https://pre-commit.com/
    * every local git commit runs all code checks and tests. 
    * every commit to `develop` runs tests and creates a build
    * example script to listen/ monitor and install latest release on `main` and `prev`
* fix logging to read a non-standard name and file location for user config file.
* development flow guideline for developing on dev branch
* add instruction how to delete jlab kernel if project/ venv is deleted


## Credits

Original inspiration and framework from [Marco Gancitano](https://github.com/mgancita/cookiecutter-pypackage), including a healthy amount of the documentation above (and links to even more documentation at his cookicutter template that I was too lazy to reproduce).

Inspiration for the `use_datascience` optional features from the [Driven Data](https://drivendata.github.io/cookiecutter-data-science/) template.

Original inspiration and the whole project not possible with Audrey Feldroy [Audrey Feldroy](https://github.com/audreyfeldroy/cookiecutter-pypackage).

See the applicable licenses in `NOTICES`.

Additional inspiration was taken from:
* [Sivaken@dev.to](https://dev.to/sivakon/python-poetry-35ec).
* Makefile and `pyproject.toml` from [Colin Dean](https://gist.github.com/colindean/9682b62ef5b3e87028bb8e23b5f4c4aa).
