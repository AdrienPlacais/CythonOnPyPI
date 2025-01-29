"""Check that all mandatory modules can be imported."""

import pytest

MODULES = (
    "argparse",
    "cloudpickle",
    "collections",
    "dataclasses",
    "functools",
    "importlib",
    "itertools",
    "math",
    "matplotlib",
    "numpy",
    "os",
    "palettable",
    "pandas",
    "pathlib",
    "pprint",
    "pre_commit",
    "pymoo",
    "scipy",
    "shutil",
    "sys",
    "tkinter",
    "typing",
)


@pytest.mark.parametrize("module_name", MODULES)
def test_module_import(module_name: str) -> None:
    """Check that ``module_name`` can be imported."""
    try:
        __import__(module_name)
    except ImportError:
        pytest.fail(f"Failed to import {module_name}")
