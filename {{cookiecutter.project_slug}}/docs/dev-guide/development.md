---
title: Development 
summary: How to develop {{ cookiecutter.project_name }}. 
authors:
    - {{ cookiecutter.full_name }} 
date: {% now 'local', '%Y-%m-%d' %}
---


## Installing from source for development

Clone the repo:

```shell
$ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
```

`Poetry` is required. Optionally set a local python version with `pyenv`.

```shell
$ pipx install poetry
$ poetry install
$ poetry info
```

Run {{cookiecutter.project_name}} from source tree on your machine:

```shell
$ poetry run python -m {{cookiecutter.project_slug}}
```

## Installing from a local build

```shell
$ make dist
```

If your package should be run as a command-line application, the recommended method is to use `pipx` so that your software and its dependencies are installed into its own isolated environment, without polluting your python interpreter's `site-packages`. This can be done with:

```bash
$ pipx install dist/<<package_name_with_version>>.tar.gz
```

or 

```bash
$ pipx install dist/<<package_name_with_version>>.whl
```


## Boilerplate

Keeping the boilerplate up to date with the original [cookiecutter template](https://github.com/smp4/cookiecutter-poetry-pypackage):

```shell
$ pipx install cruft
$ cruft check
$ cruft update
```

Run the checks and tests:

``` shell
$ make checks
$ make test
```

## Development Flow

This project uses the [OneFlow](https://www.endoflineblog.com/implementing-oneflow-on-github-bitbucket-and-gitlab) workflow. Follow the link for GitHub implementation.

Rationale:

* Conform to Open Source norms. Provide a `main` branch containing the latest stable release.
* Relatively linear Git history.
* Single long-lived branch rather than lots of merging between parallel branches (long lived release, main and develop branches). Less maintenance overhead, faster iterations.
* Simple for one person projects, as well as collaboration.


Assumptions for use: 

1. Every new production release is based on the previous release. As soon as there are breaking changes (ie. 1.x to 2.x), the flow breaks down. Best to move v2.x to a new repo. 
2. The project does not need to maintain multiple simultaneous but incompatible release versions (ie. users are always interested in the latest release).
3. Releases are not super frequent (ie. Not Continuous Deployment). Control deployment by creating releases and pointing to them on `main` rather than continuously deploying `develop` to production. Allow more extensive one-developer team testing with `develop` deploying to staging environment. 


**Branches**

1. `develop`, the primary long-lived branch. Lives on the public repo. It is the `single source of truth`. 
2. `main`, always points to the latest stable release for ease of collaboration on open source projects (users normally expect `main` to contain the latest stable release). It just points to the latest release on `develop`. Lives on the public repo. `main` always points to a production-ready version. It is a convenience branch.
3. `feature/xxx` feature branches. Short-lived, and always merge back to main, then are deleted. Normally only lives on local machines or pushed to private repos (forks of the origin) for backup or collaboration.
4. `release-xxx` release branches. For cutting and preparing a new release from `develop` with version bumping, extra tests, QA etc. Always merges back to `develop` and `main`, then gets deleted. Releasing takes place on a separate branch so that development can continue. Exists on the origin repo.
5. `hotfix-xxx` hotfix branches. Same as release branches but started at the last commit of the latest stable release instead of a given state of `develop`. Deleted once released and merged back to `develop` and `main`. Exists on the origin repo.

In short, only `develop` and `main` are long-lived and `develop` always reflects the latest feature status. Nightly builds could be built from `develop`. Other branches are short-lived. 


In principle, `develop` should always be in a state ready to be deployed to production. Nothing should be merged to `develop` unless it is fully tested. Production services can monitor `main` for updates and automatically deploy the update when they see it.

**Merging**

Merges are done by `merge --squash`ing. This keeps the Git history linear and cleaner on `develop`. 


**Tags**

Tags are used to denote releases. If the `main` branch variation isn't used, then tags are the only way to find the stable releases.

**Commit Notation**
TODO.

**Optional**

You may add a `prev` branch that always points to the *previous* stable version, to allow your production services to quickly revert to the old release if they detect something going wrong.

**Environments**

Think about them....

eg. Consider running a staging environment that is identical to production, including production-like data and access, except it has no business consequences if something goes wrong. Might also be considered testing. Staging could continuously monitor the `develop` branch for updates and automatically install the latest version. 


**CI**

* Merge to main daily.
* Automate the build. Make the build fast.
* Make the build self-testing. 
* Every commit builds (and therefore tests). 
* Always test in a clone of the production environment. 
* Automate deployment. 


The team never checks in broken or untested code to `develop`. It is always checked locally first. The integration server also runs every commit through the test suite and creates a build artefact that could be potentially deployed.

This makes sure that ideally, `develop` is always ready for production (continuous deployment).
