import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    
    row=len(A)
    col=len(A[0])
    sum=0
    for i in range(row):
        for j in range(col):
           if i==j:
               sum=sum+A[i][j]
    return sum


# def matrix_trace(A: list) -> float:
#     """
#     Returns the trace as a float.
#     """
#     trace = 0
#     for i in range(len(A)):
#         trace += A[i][i]  
#     return float(trace)
               