# Cython on PyPI

A test package for distributing Cython on (Test)PyPI.

## CI

The `.github/workflows/CI.yml` allows to test the package with gh actions.

## Manual release

The commands in `make pypi` would allow publishing a *tagged* version of the package on PyPI.
The thing is, with Cython compiled, the wheel file is refused.
Note that uploading the `.tar.gz` works.
