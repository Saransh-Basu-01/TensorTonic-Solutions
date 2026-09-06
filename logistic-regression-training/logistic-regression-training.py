import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    w = np.zeros(X.shape[1])
    b = 0.0 
    n = X.shape[0]
    for i in range(steps):
        z=np.dot(X,w)+b
        z=_sigmoid(z)
        loss = -np.mean(y * np.log(z ) + (1 - y) * np.log(1 - z))
        dLoss=z-y
        dLoss_dw=np.dot(X.T,dLoss)/n
        dLoss_db=np.mean(dLoss)
        w=w-lr*dLoss_dw
        b=b-lr*dLoss_db
    return w,b
