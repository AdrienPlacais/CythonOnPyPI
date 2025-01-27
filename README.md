# Cython on PyPI

A test package for distributing Cython on (Test)PyPI.

## CI

The `.github/workflows/CI.yml` allows to test the package with gh actions.

## Manual release

The commands in `make pypi` would allow publishing a *tagged* version of the package on PyPI.
The thing is, with Cython compiled, the wheel file is refused (`.whl`, built distribution).
Note that uploading the `.tar.gz` (source distribution) works.

## `setuptools_scm`

Automates the version number in `pyproject.toml`, according to the tag.
Note that if cython updates the `.c` file and this file is tracked, building the wheel will update the repo.
So `setuptools_scm` will set a new local version number: `vX.Y.Z+dev0-slkfjslfjas-sdnalkd` instead of desired `vX.Y.Z`.
Current workaround is removing `.c` files from repo.

## CD

Using `cibuildwheel` seems to be the easiest solution.
Most of it is configured in `pyproject.toml`.
Note that Windows will not interpret single quotes correctly.
The `tool.cibuildwheel.test-command` must be `'pytest {project}/tests -m "my_mark"'` (do not invert the single and double quotes).
