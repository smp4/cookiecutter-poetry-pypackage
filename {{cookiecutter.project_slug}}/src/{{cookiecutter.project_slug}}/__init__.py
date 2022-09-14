# {{ cookiecutter.project_slug }}/__init__.py
# This file is part of {{cookiecutter.project_name}}.
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.full_name}}.
# Contact: {{cookiecutter.email}}
# See the LICENSE file distributed with this software.

"""{{ cookiecutter.project_name }} namespace.

Modules exported by this package:
    - `module1`: Short description of the module.

"""

import logging

from importlib_metadata import PackageNotFoundError, version

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"

# In the absence of application level logging configuration, send all logs sent
# by the library to the do-nothing handler.
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Used to automatically set version number from github actions
# as well as not break when being tested locally
try:
    __version__ = version(__package__)  # type: ignore
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.1.0"
