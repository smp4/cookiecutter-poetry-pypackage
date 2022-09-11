"""Module to clean up generated repository post generation."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove file at given filepath."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    # rename .env_template to .env after cookie is baked
    os.rename(".env_template", ".env")

    # AUTHORS
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")
        remove_file("docs/about/authors.md")

    # LICENSE
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")

    # GitHub Actions
    if "{{ cookiecutter.use_github_actions_for_ci }}" != "y":
        remove_file(".github/workflows/code_quality_checks.yml")

    if "{{ cookiecutter.use_github_actions_to_publish_docs }}" != "y":
        remove_file(".github/workflows/docs_publish.yml")

    if "{{ cookiecutter.use_github_actions_for_pypi_deployment }}" != "y":
        remove_file(".github/workflows/pypi_publish.yml")
        remove_file(".github/workflows/test_pypi_publish.yml")

    # CI Checks
    if "{{ cookiecutter.use_flake8 }}" != "y":
        remove_file(".flake8")

    #    if "{{ cookiecutter.use_mypy }}" != "y":
    #       remove_file("mypy.ini")

    if "{{ cookiecutter.use_yamllint }}" != "y":
        remove_file("yamllint-config.yml")

    # Datascience directories
    if "{{ cookiecutter.use_datascience }}" != "y":
        remove_file("data/")
        remove_file("models/")
        remove_file("references/")

    # Jupyter directories
    if "{{ cookiecutter.use_jupyter }}" != "y":
        remove_file("notebooks/")
        remove_file("reports/")
