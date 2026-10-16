import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n=len(x)
    x=np.asarray(x)
    x_mean=np.mean(x)
    variance=float((1/(n-1))*np.sum((x-x_mean)**2))
    std=float(np.sqrt(variance))
    return {
        "variance":variance,
        "standard_deviation":std
    }
    