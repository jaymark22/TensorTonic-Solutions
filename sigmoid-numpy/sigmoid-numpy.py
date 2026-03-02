import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    1/(1+ np.exp(-x))
    """
    x = np.asarray(x, dtype=np.float64)
    return 1.0 / (1.0 + np.exp(-x))