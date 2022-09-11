# {{ cookiecutter.project_slug }}/pysource_template.py
# This file is part of {{cookiecutter.project_name}}.
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.full_name}}.
# Contact: {{cookiecutter.email}}
# See the LICENSE file distributed with this software.


"""One line description of module.

Describe what the module does.

Examples:
    >>> from x import y
    >>> newfile.function1(a, b)
    2.0

The module contains the following functions:

- `function1(a, b)`: returns the sum of two numbers.
"""

import logging
import sys

# from x import y  # importing from dependencies
# from . import adjacent_sourcefile  # relative imports inside the package
# ...

log = logging.getLogger(__name__)


# To run a package source file as a script, check if it is being run as main:
def main():
    """Example main function. Replace it with library code."""

    print("This file is being run as the main program.")
    log.debug("Inside the main program in the template file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
