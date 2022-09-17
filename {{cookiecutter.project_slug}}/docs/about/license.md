{% set project_github_link = cookiecutter.project_slug | replace("_", "-") -%}

Licensed with {{ cookiecutter.open_source_license }}. Check the [LICENSE](https://{{ cookiecutter.github_username }}/{{ project_github_link }}/blob/main/LICENSE) in the source code.
