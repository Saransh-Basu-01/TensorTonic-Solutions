import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix=np.array(matrix)
    if norm_type == "l1":
        if axis == 0:
            sum = np.sum(matrix, axis=0,keepdims=True)
            sum = np.where(sum == 0, 1, sum)
            matrix = matrix / sum
            return matrix
            
        if axis==1:
            sum=np.sum(matrix,axis=1,keepdims=True)
            sum = np.where(sum == 0, 1, sum)
            matrix=matrix/sum
            return matrix

        if axis is None:
            sum = np.sum(np.abs(matrix))
            sum = np.where(sum == 0, 1, sum)
            matrix = matrix / sum
            return matrix
            
    elif norm_type=="l2":
        if axis==0:
            sqrt = np.sqrt(np.sum(matrix**2, axis=0, keepdims=True))
            sqrt = np.where(sqrt == 0, 1, sqrt)
            matrix=matrix/sqrt
            return matrix
            
        if axis==1:
            sqrt = np.sqrt(np.sum(matrix**2, axis=1, keepdims=True))
            sqrt = np.where(sqrt == 0, 1, sqrt)
            matrix=matrix/sqrt
            return matrix
            
        if axis is None:
            sqrt = np.sqrt(np.sum(matrix**2))
            sqrt = np.where(sqrt == 0, 1, sqrt)
            matrix = matrix / sqrt
            return matrix

            
    elif norm_type=="max":
        if axis == 0:
            max_val = np.max(np.abs(matrix), axis=0,keepdims=True)
            max_val = np.where(max_val == 0, 1, max_val)
            matrix = matrix / max_val
            return matrix
    
        if axis == 1:
            max_val = np.max(np.abs(matrix), axis=1,keepdims=True)
            max_val = np.where(max_val == 0, 1, max_val)
            matrix = matrix / max_val
            return matrix

        if axis is None:
            max_val = np.max(np.abs(matrix))
            max_val = np.where(max_val == 0, 1, max_val)
            matrix = matrix / max_val
            return matrix

    else:
        return np.array([])
    