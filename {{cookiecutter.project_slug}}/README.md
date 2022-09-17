{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% set project_github_link = cookiecutter.project_slug | replace("_", "-") -%}

# {{ cookiecutter.project_name }}

> *{{ cookiecutter.project_short_description }}*

![versions](https://img.shields.io/pypi/pyversions/{{ project_github_link }}.svg){% if cookiecutter.use_black %}[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black){% endif %}

{% if is_open_source %}
- Free software: {{ cookiecutter.open_source_license }}
{%- endif %}
- Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ project_github_link }}.
- Source code: https://{{ cookiecutter.github_username }}/{{ project_github_link }}

## What is it?
{{ cookiecutter.project_name }} provides/ does/ gives ...


Please see the Documentation for introductory tutorials and user guide.

## Main Features

What are the main features?


## Installation 

See the docs.

## Development and Contributing

Contributions from others would be great. See the Development guide in the docs for how to get started and help out.
Bug reporting and feature requests are welcome! Please open an issue on GitHub <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues>.

## License
{{ cookiecutter.open_source_license }}. See [LICENSE](https://{{ cookiecutter.github_username }}/{{ project_github_link }}/blob/main/LICENSE).

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) using [cookiecutter-poetry-pypackage](https://github.com/smp4/cookiecutter-poetry-pypackage).

