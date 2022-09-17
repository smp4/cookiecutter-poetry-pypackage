# {{ cookiecutter.project_slug }}/logsetup.py
# This file is part of {{cookiecutter.project_name}}.
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.full_name}}.
# Contact: {{cookiecutter.email}}
# See the LICENSE file distributed with this software.

"""Sets up logging to stdout, stderr when run as an app."""

import logging
import logging.config
import os
import sys
import time

import yaml

logger = logging.getLogger(__name__)


# default format string of a log message
FORMAT_STR = (
    "%(asctime)UTC|PID"
    "%(process)d|%(processName)s|%(name)s|%(levelname)s|%(message)s"
    "(%(filename)s:%(lineno)d)"
)


# https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
# https://docs.python.org/3/howto/logging-cookbook.html#customized-exception-formatting
class ColouredFormatter(logging.Formatter):
    """Custom formatter providing coloured output to console.

    Also converts message time to UTC and prints exceptions as a single
    line.

    """

    logging.Formatter.converter = time.gmtime

    grey = "\x1b[38;20m"
    white = "\x1b[37;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: white + FORMAT_STR + reset,
        logging.INFO: green + FORMAT_STR + reset,
        logging.WARNING: yellow + FORMAT_STR + reset,
        logging.ERROR: red + FORMAT_STR + reset,
        logging.CRITICAL: bold_red + FORMAT_STR + reset,
    }

    def formatException(  # type: ignore
        self, ei
    ) -> str:  # pylint: disable=no-member
        """Format an exception so that it prints on a single line."""
        result = super().formatException(ei)
        return repr(result)  # or format into one line however you want to

    def format(self, record: logging.LogRecord) -> str:
        """Reformat exception as single line and apply colouring."""
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        out_str = formatter.format(record)
        if record.exc_text:
            out_str = out_str.replace("\n", "") + "|"
        return out_str


class PlainFormatter(logging.Formatter):
    """Plain formatting, no colour.

    Plain formatting, no colour. Also converts message time to UTC.

    """

    logging.Formatter.converter = time.gmtime

    def format(self, record: logging.LogRecord) -> str:
        """Apply UTC and format string."""
        formatter = logging.Formatter(FORMAT_STR)
        return formatter.format(record)


# https://stackoverflow.com/questions/1383254/logging-streamhandler-and-standard-streams
class MaxLevelFilter(logging.Filter):  # pylint: disable=too-few-public-methods
    """Filters (lets through) all messages with level < LEVEL."""

    def __init__(self, level: int) -> None:
        """Set the debug level at initialisation."""
        super().__init__("")
        self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        """Allow messages with level < LEVEL."""
        return (
            record.levelno < self.level
        )  # "<" instead of "<=": since logger.setLevel is inclusive, this should be exclusive


def default_log_config(
    log: logging.Logger, default_level: int = logging.DEBUG
) -> None:
    """Apply  the default log configuration.

    DEBUG and INFO logs to stdout, WARNING and higher to stderr. By default
    colours the output for the terminal. Can be turned off in `logsetup.py` if
    the colour escape strings mess with your application.

    Assumes that the application passes all logs up to the RootLogger to be
    processed.

    Args:
        log: The logger to be configured.
        default_level: The minimum message level that the logger should process.
    Returns:
        None

    """
    stdout_hdlr = logging.StreamHandler(sys.stdout)
    stderr_hdlr = logging.StreamHandler(sys.stderr)
    lower_than_warning = MaxLevelFilter(level=logging.WARNING)
    stdout_hdlr.addFilter(lower_than_warning)

    stdout_hdlr.setLevel(logging.DEBUG)  # messages < WARNING go to stdout
    stderr_hdlr.setLevel(logging.WARNING)  # messages >= WARNING go to stderr

    log.addHandler(stdout_hdlr)
    log.addHandler(stderr_hdlr)
    log.setLevel(default_level)

    #    rootLogger = logging.getLogger()
    #    rootLogger.addHandler(stdout_hdlr)
    #    rootLogger.addHandler(stderr_hdlr)
    #    rootLogger.setLevel(MIN_LEVEL)

    use_colours = True  # Set to False to use standard formatter with no colour

    if use_colours:
        stdout_hdlr.setFormatter(ColouredFormatter())
        stderr_hdlr.setFormatter(ColouredFormatter())
    else:
        stdout_hdlr.setFormatter(PlainFormatter())
        stderr_hdlr.setFormatter(PlainFormatter())


#    stream_handler = logging.StreamHandler()
#    stream_handler.setFormatter(formatter)
#    log.addHandler(stream_handler)


def setup_logging(
    log: logging.Logger,
    default_path: str = "resources/logging.yml",
    default_level: int = logging.DEBUG,
    env_key: str = "LOG_CFG",
) -> None:
    """Set up the logging configuration.

    By default, uses the setup in code `default_log_config`. If a file
    `resources/logging.yml` exists in the directory where the application is
    executed, or a relative path is given to such a file, then that file will
    be loaded and used to configure the logging. Finally, you command also set
    LOG_CFG environment variable to load the logging configuration from a path.

    Args:
        log:            The logger to be configured.
        default_path:   Location of the yaml logging configuration file.
        default_level:  Default logging level (ie. "logging.WARN"). Defaults to
        DEBUG. These evaluate to integers.
        env_key:        Environment variable within which a custom path to the
        logging config file can be stored.

    Expected usage:
        Assuming `{{cookiecutter.project_slug}}` has been installed,
        `LOG_CFG=/path/to/my_logging.yml python {{cookiecutter.project_slug}}`

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        logger.debug("path exists")
        with open(path, "rt", encoding="utf-8") as file:
            config = yaml.safe_load(file.read())
            try:
                logging.config.dictConfig(config)
                logger.debug("Logging configured from file.")
            except (ValueError, KeyError):
                logger.exception(
                    (
                        "Unable to load the configuration from file, contains "
                        "configuration error."
                    )
                )
                # When there is an error in the config, escalate the exception,
                # otherwise the application would silently fall back on the
                # default config.
                raise
    else:
        try:
            default_log_config(log, default_level)
            logger.debug("Logging configured from default.")
        except (ValueError, KeyError):
            logger.exception(
                ("Unable to load the default configuration from "
                 "default_log_config, contains configuration error.")
            )
            raise
