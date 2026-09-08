import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    y_pred_clipped=[min(1-eps,max(eps,p)) for p in y_pred]
    loss=[-(yt*math.log(yp)+(1-yt)*math.log(1-yp)) for yt,yp in 
          zip(y_true,y_pred_clipped)]
    return loss