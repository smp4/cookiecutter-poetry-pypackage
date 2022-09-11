# This file is part of {{cookiecutter.project_name}}.
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.full_name}}.
# Contact: {{cookiecutter.email}}
# See the LICENSE file distributed with this software.

"""Test module for {{cookiecutter.project_slug}}."""

from {{cookiecutter.project_slug}} import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "{{cookiecutter.full_name}}"
    assert __email__ == "{{cookiecutter.email}}"
    assert __version__ == "0.1.0"
