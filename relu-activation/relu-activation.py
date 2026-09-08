import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    if isinstance(x, (int, float, complex, bool)):
        x = np.array(max(0, float(x)))
    else:
        x = np.array(x, dtype=float)
        x = np.maximum(0, x)
    
    return x
