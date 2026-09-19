import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    if not seqs:
        return np.zeros((0, 0), dtype=int)
    
    L = max_len if max_len is not None else max(len(seq) for seq in seqs)
    
    padded = []
    for seq in seqs:
        seq = list(seq)[:L]         
        diff = L - len(seq)
        if diff > 0:
            seq.extend([pad_value] * diff)   
        padded.append(seq)
    
    return np.array(padded, dtype=int)