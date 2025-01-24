"""Check that Python version of degrees works as expected."""

import numpy as np
import pytest

from cython_on_pypi.converters.degrees import to_fahrenheit


def test_degrees() -> None:
    """Check on some values."""
    celsius = np.array([-20.0, 0.0, 35.0])
    expected = np.array([-4.0, 32.0, 95.0])
    returned = to_fahrenheit(celsius)
    assert expected == pytest.approx(returned)
