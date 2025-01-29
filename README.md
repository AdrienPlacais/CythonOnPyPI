# Cython on PyPI

A test package for distributing Cython on (Test)PyPI.

## CI

The `.github/workflows/CI.yml` allows to test the package with gh actions.

## CD

Using `cibuildwheel` seems to be the easiest solution.
Most of it is configured in `pyproject.toml`.
Note that Windows will not interpret single quotes correctly.
The `tool.cibuildwheel.test-command` must be `'pytest {project}/tests -m "my_mark"'` (do not invert the single and double quotes).

## Manual release (use CD instead)

The commands in `make pypi` would allow publishing a *tagged* version of the package on PyPI.
The thing is, with Cython compiled, the wheel file is refused (`.whl`, built distribution).
Note that uploading the `.tar.gz` (source distribution) works.

## `setuptools_scm`

Automates the version number in `pyproject.toml`, according to the tag.
Note that if cython updates the `.c` file and this file is tracked, building the wheel will update the repo.
So `setuptools_scm` will set a new local version number: `vX.Y.Z+dev0-slkfjslfjas-sdnalkd` instead of desired `vX.Y.Z`.
Current workaround is removing `.c` files from repo.

## Reproduce LW error

### Packages that I can install
Listing Python packages that I managed to install.
- [x] `cloudpickle`
- [x] `matplotlib`
- [x] `pandas`
- [x] `palettable`
- [x] `pre-commit`
- [x] `pymoo`
- [x] `scipy`
- [ ] `tkinter` (sometimes problematic, not checked yet)

### Distributions that have a problem with unchecked previous packages
(test on `scipy`)
- [x] `macos-13`
- [x] `macos-latest`
- [x] `ubuntu-latest`
- [ ] `ubuntu-24.04-arm` (last problematic OS)
- [x] `windows-latest`

### Notes
- Putting the packages in `[build-system].requires` also creates the failure.
- The thing is that it tries to build the `.tar.gz` dependencies instead of using the `.whl`.
    - Note that `matplotlib 3.10.0-cp312-cp312` does not exit in compiled version for 32 bit Windows.

> [!IMPORTANT]
> On `windows-latest`, the solution was to set `[tools.cibuildwheel].archs = "auto64"`.
> As the wheel did not exist in 32-bits, gh actions tried to build it but did not have the required tools.
