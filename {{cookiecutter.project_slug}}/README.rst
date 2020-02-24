{{ cookiecutter.project_name }}
===========================================

{{ cookiecutter.project_short_description }}


version numbering
-----------------

The version needs to be recorded in several places, so do this to make a release:

0. Have a clean git checkout (git stash or commit any uncommitted changes)
1. Update pyproject.toml with poetry
2. Update other files with bump2version

First bump the version in pyproject.toml

During development make sure to use:

poetry version prerelease  # 0.0.0-alpha.X

Or specify which version is going to be bumped with
poetry version premajor  # X.0.0-alpha.0
poetry version preminor  # 0.X.0-alpha.0
poetry version prepatch  # 0.0.X-alpha.0

Or for a production release:

poetry version major  # X.0.0
poetry version minor  # 0.X.0
poetry version patch  # 0.0.X

Second update everywhere else (all changes will be committed):

git add pyproject.toml
poetry run bump2version . --new-version $(poetry version | cut -d' ' -f2) --allow-dirty

bump2version should update 4 files, commit them, and add a git tag:

- .bumpversion.cfg
- src/tsync/__init__.py
- tests/test_tsync.py
- docs/source/conf.py

Using Poetry
------------

https://poetry.eustace.io/docs/

Jacob Floyd:

> During development, I like to keep my virtualenvs in ~/v, so I ran this:
>   poetry config virtualenvs.path ~/v
> However, for deployments, where we want a standardized virtualenv location,
> we should create and activate our desired virtualenv before running poetry.

Using tox and pytest
--------------------

To run the tests, run tox, and let tox run pytest

poetry run tox -e py37

Build sphinx docs via tox
-------------------------

poetry run tox -e docs
