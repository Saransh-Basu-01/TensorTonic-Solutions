import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    positions = np.arange(seq_len).reshape(seq_len, 1)                        
    i = np.arange(np.ceil(d_model / 2).astype(int)).reshape(1, -1)            
    frequencies = 1.0 / (base ** (2 * i / d_model))                           
    angles = positions * frequencies                                          
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angles)                                              
    pe[:, 1::2] = np.cos(angles)[:, :pe[:, 1::2].shape[1]]                    
    return pe