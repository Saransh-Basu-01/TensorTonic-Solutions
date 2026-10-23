import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    rng = np.random.default_rng(seed)
    x=np.asarray(x)
    resampled_means=[]
    for i in range(n_bootstrap):
        sample = rng.choice(x, size=len(x), replace=True)
        resampled_means.append(np.mean(sample))
    total_mean=np.mean(resampled_means)
    alpha=(1-ci)/2
    lower=np.quantile(resampled_means,alpha)
    upper=np.quantile(resampled_means,1-alpha)
    return {
        "bootstrap_mean":total_mean,
        "lower":lower,
        "upper":upper
    }