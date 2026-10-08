import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    if rng is None:
        rng=np.random.default_rng()
    x_np=np.array(x)
    random=rng.random(size=x_np.shape)
    mask=(random >= p).astype(float)
    dropout_pattern = mask / (1-p)
    output=x_np*dropout_pattern
    print(x_np.shape, random.shape, dropout_pattern.shape)
    return (output,dropout_pattern)