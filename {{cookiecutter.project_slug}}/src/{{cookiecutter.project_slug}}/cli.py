# {{ cookiecutter.project_slug }}/cli.py
# This file is part of {{cookiecutter.project_name}}.
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.full_name}}.
# Contact: {{cookiecutter.email}}
# See the LICENSE file distributed with this software.

"""Entry point module for `python -m{{cookiecutter.project_slug}}`.

Why does this file exist, and why not put this in __main__?

You might be tempted to import things from __main__ later, but that will cause
problems: the code will get executed twice:
  - When you run `python -m{{cookiecutter.project_slug}}` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``{{cookiecutter.project_slug}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``{{cookiecutter.project_slug}}.__main__`` in ``sys.modules``.

Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration

Sets up basic logging for the CLI entry point. By default, also loads an .env
file.

Examples:
    >>> python -m {{ cookiecutter.project_slug }}
    >>> poetry shell && {{ cookiecutter.project_slug }}
"""

{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- elif cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys, logging


logger = logging.getLogger(__name__)

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
@click.argument('names', nargs=-1)
def main(names):
    """Console script for {{cookiecutter.project_slug}}."""
    logger.debug('Using Click.')

    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    click.echo(repr(names))
    return 0

{%- elif cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    logger.debug('Using Argparse.')

    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0

{%- else %}
def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments
    Returns:
        int: A return code
    Does stuff.
    """
    print(argv)
    return 0
{%- endif %}
