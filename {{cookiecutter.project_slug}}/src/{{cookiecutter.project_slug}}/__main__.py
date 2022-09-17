# {{ cookiecutter.project_slug }}/__main__.py
# This file is part of {{cookiecutter.project_name}}.
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.full_name}}.
# Contact: {{cookiecutter.email}}
# See the LICENSE file distributed with this software.

"""Entrypoint module, in case using `python -m {{cookiecutter.project_slug}}`.

Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m

"""

import logging
{% if ( cookiecutter.command_line_interface|lower != 'click' ) and
      (  cookiecutter.command_line_interface|lower != 'argparse' ) -%}
import sys
{%- endif %}
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

from . import cli, logsetup

if __name__ == "__main__":
    try:
        log = logging.getLogger(__name__)
        logsetup.setup_logging(default_level=logging.DEBUG)
        log.debug("Logging is set up and configured.")

        # test coloured logging
        log.debug("Test debug message, should be white.")
        log.info("Test info message, should be green.")
        log.warning("Test warning message, should be yellow.")
        log.error("Test error message, should be red.")
        log.critical("Test critical message, should be bold red.")

        # now test single line exception log text
        # remember to use log.<<exception>> for exceptions, to get the stack
        # trace.
        try:
            x = 1 / 0
        except ZeroDivisionError:
            log.exception("Can't divide by zero!")

        # not used in this stub but often useful for finding various files
        project_dir = Path(__file__).resolve().parents[2]

        # find .env automagically by walking up directories until it's found, then
        # load up the .env entries as environment variables
        load_dotenv(find_dotenv())

        {% if ( cookiecutter.command_line_interface|lower == 'click' or
               cookiecutter.command_line_interface|lower == 'argparse' ) -%}
        cli.main()
        {%- else %}
        sys.exit(cli.main())  # pragma: no cover
        {%- endif %}
    except Exception:  # pylint: disable=broad-except
        log.exception("Fatal error in main loop.")
