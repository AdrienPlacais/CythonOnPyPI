cimport numpy as cnp
import numpy as np


def to_fahrenheit(cnp.ndarray[cnp.float64_t, ndim=1] celsius):
    """Convert an array of Celsius values to Fahrenheit.

    Parameters
    ----------
    celsius : numpy.ndarray
        Input array of Celsius temperatures.

    Returns
    -------
    numpy.ndarray
        Array of Fahrenheit temperatures.

    """
    cdef int n = celsius.shape[0]
    cdef cnp.ndarray[cnp.float64_t, ndim=1] fahr = np.empty(n, dtype=np.float64)
    cdef int i

    for i in range(n):
        fahr[i] = celsius[i] * 1.8 + 32

    return fahr
