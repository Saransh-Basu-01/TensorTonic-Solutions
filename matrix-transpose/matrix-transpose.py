import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # return np.array(A).T
    if not A or not A[0]:
        return np.array([])
    
    rows = len(A)
    cols = len(A[0])
    result = np.zeros((cols, rows))
    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j] 
    return result