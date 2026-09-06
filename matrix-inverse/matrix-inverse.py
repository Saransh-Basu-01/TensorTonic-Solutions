import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    row=len(A)
    col=len(A[0])
    # if row == 1:
    #     return np.array([[1 / A[0][0]]])
    det=np.linalg.det(A)
    if row!=col or det==0:
        return
    #only for 2d matrix 
    # a, b = A[0]
    # c, d = A[1]
    # inverse=(1/det) * np.array([
    #     [d,-b],
    #     [-c,a]
    # ])
    #applicable to all
    inverse = np.linalg.inv(A)
    return inverse
    