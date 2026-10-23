import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    center=size//2
    kernel=[]
    for i in range(size):
        row=[]
        for j in range(size):
            x=i-center
            y=j-center
            weight = math.exp(-(x**2 + y**2) / (2 * sigma**2))
            row.append(weight)
        kernel.append(row)

    total=0
    for i in range(size):
        for j in range(size):
            total=total+kernel[i][j]
    
    for i in range(size):
        for j in range(size):
            kernel[i][j]/=total

    return kernel
        
            
            