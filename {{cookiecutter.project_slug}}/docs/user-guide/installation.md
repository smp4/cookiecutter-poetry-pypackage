---
title: Installation 
summary: How to install {{ cookiecutter.project_name }}. 
authors:
    - {{ cookiecutter.full_name }} 
date: {% now 'local', '%Y-%m-%d' %}
---

!!! warning

    Installation instructions not implemented yet!


## Installing the Stable Release from PyPI

To install {{ cookiecutter.project_name }}, run this command in your terminal:

``` console
$ pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install {{ cookiecutter.project_name}}, as it will always install the most recent stable release. You can also replace `pip` with `pipx`.


## Installing From source

The source for {{ cookiecutter.project_name }} can be downloaded from the GitHub repo. The recommended installation method to add {{ cookiecutter.project_name }} as dependency, from source, to your project is to use `Poetry`:

``` shell
$ poetry add git+ssh://git@github.com:usr/package_name.git#main
```

To install {{ cookiecutter.project_name }} as a command line application, use `pipx` (which isolates it into its own environment):

```shell
$ pipx install git+ssh://git@github.com:usr/package_name
```

Of course, you can always clone the repository from source as well:

``` console
$ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```


## Logging
{{cookiecutter.project_name}} uses the standard Python `logging` module.

When imported as a library, all logs are sent to the NULL handler (ie. *no logs* are communicated to the user) unless the calling application has set up its own log handling. See the [`logging` docs](https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library).


When {{ cookiecutter.project_name }} is run as an application, for example with `python -m {{ cookiecutter.project_slug }}`, a default log configuration is applied which will send all logs lower than `WARNING` to `stdout` and `WARNING`, `ERROR`, `CRITICAL` to `stderr`.

!!! warning
    User configuration file setup of logging is not fully implemented. A config
    file name and path that doesn't match the example below will not work. 

The user may apply their own custom formatting via a `logging.yml` file which must be stored in the `resources` directory inside the directory from which {{cookiecutter.project_slug}} is executed. Alternatively, if the logging file is stored elsewhere, it can be passed through via environment variable with

```shell
$ LOG_CFG=/path/to/my_logging.yml python {{cookiecutter.project_slug}}
```

An example `logging.yml` configuration file is given below:

```yaml
---
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: "%(asctime)s|<PID %(process)d|%(processName)s>|%(name)s|%(levelname)s|%(message)s"

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout

root:
  level: DEBUG
  handlers: [console]
```

See the `logsetup.py` module for more details.

