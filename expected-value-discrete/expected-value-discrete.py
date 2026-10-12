import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    result=sum((xi*pi for xi,pi in zip(x,p)))
    return float(result)