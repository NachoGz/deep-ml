import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    id = (np.arange(len(a)) * 0) + 1
    return np.dot(a, id)
