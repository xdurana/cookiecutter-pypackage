# Cookiecutter PyPackage

[![Supported Python versions](https://img.shields.io/pypi/pyversions/cookiecutter-pypackage)](https://pypi.org/project/cookiecutter-pypackage/)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://xdurana.github.io/cookiecutter-pypackage/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/cookiecutter-pypackage)](https://img.shields.io/pypi/dm/cookiecutter-pypackage?style=flat-square)

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
repository to generate the file structure for a Python project that uses
[Poetry](https://python-poetry.org/) for its dependency management.

- **Documentation**: [Link](https://xdurana.github.io/cookiecutter-pypackage/)
- **Example repository**: [Link](https://github.com/xdurana/cookiecutter-pypackage-example)
- **PyPi**: [Link](https://pypi.org/project/cookiecutter-pypackage/)

## Features

- [Poetry](https://python-poetry.org/), obviously.
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Formatting with [black](https://pypi.org/project/black/) and [isort](https://pycqa.github.io/isort/index.html)
- Linting with [flake8](https://flake8.pycqa.org/en/latest/)
- Publishing to [Pypi](https://pypi.org) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Static type checking with [mypy](https://mypy.readthedocs.io/en/stable/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)
- Containerization with [Docker](https://www.docker.com/)

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

``` bash
pip install cookiecutter-pypackage
ccp
```

Alternatively, install `cookiecutter` and directly pass the URL to this
Github repository to the `cookiecutter` command:

``` bash
pip install cookiecutter
cookiecutter https://github.com/xdurana/cookiecutter-pypackage.git
```

Then run the following commands, replacing `<project-name>`, with the
name that you also gave the Github repository and
`<github_author_handle>` with your Github username.

``` bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment with `make install`.

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://xdurana.github.io/cookiecutter-pypackage/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://xdurana.github.io/cookiecutter-pypackage/features/mkdocs/#enabling-the-documentation-on-github).

## Acknowledgements

This project is partially based on [Audrey
Feldroy's](https://github.com/audreyfeldroy) great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) and [
Florian Maas](https://github.com/fpgmaas/) great [cookiecutter-pypackage](https://github.com/fpgmaas/cookiecutter-pypackage).
