import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    len_v=len(v)
    mat=np.zeros((len_v,len_v))
    for i in range(len_v):
        mat[i, i] = v[i]
    return mat
    