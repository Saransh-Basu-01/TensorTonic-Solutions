import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    if isinstance(x, list):
        x = np.array(x)
        
    if np.isscalar(x):
        return float(1 / (1 + np.exp(-x)))
                     
    return 1/(1+np.exp(-x))