"""Convert celsius to fahrenheit."""

import numpy as np


def to_fahrenheit(celsius: np.ndarray) -> np.ndarray:
    """Convert degrees."""
    fahr = celsius * 1.8 + 32
    return fahr
