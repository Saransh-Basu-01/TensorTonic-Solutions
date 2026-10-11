import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    T=np.asarray(T,dtype=float)
    p = np.asarray(points, dtype=float)
    if p.ndim == 1:                      # (3,)
        p = np.append(p, 1.0)
    elif p.ndim == 2:                    # (N, 3)
        p = np.hstack([p, np.ones((p.shape[0], 1))])
    else:
        raise ValueError(f"Unsupported shape: {p.shape}")

    result=(T @ p.T).T
    return result[..., :3]  
    
    