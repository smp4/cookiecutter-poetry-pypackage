"""Module to clean up generated repository post generation."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove file at given filepath."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    os.system("tree -aL 2")

    # rename .env_template to .env after cookie is baked
    os.rename(".env_template", ".env")

    # rename data_template dir to data after cookie is baked
    os.system("mv data_template data")
    os.system("tree -aL 2")

    # AUTHORS
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")

    # LICENSE
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")

    # CI Checks
    if "{{ cookiecutter.use_flake8 }}" != "y":
        remove_file(".flake8")

    if "{{ cookiecutter.use_yamllint }}" != "y":
        remove_file("yamllint-config.yml")

    # Datascience directories
    if "{{ cookiecutter.use_datascience }}" != "y":
        remove_file("data")
        remove_file("models/")
        remove_file("references/")

    # Jupyter directories
    if "{{ cookiecutter.use_jupyter }}" != "y":
        remove_file("notebooks/")
        remove_file("reports/")
