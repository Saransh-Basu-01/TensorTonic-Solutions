import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    relu=[]
    for i in x:
        if i >=0:
            relu.append(i)
        else:
            relu.append(alpha*i)
    relu=np.array(relu)
    return relu
        