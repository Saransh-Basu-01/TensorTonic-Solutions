import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x=np.array(x,dtype=float)
    y=np.array(y,dtype=float)
    res=np.dot(x,y)
    res=float(res)
    return res