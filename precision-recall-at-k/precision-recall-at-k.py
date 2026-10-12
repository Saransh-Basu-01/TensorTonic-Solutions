def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    top_k=recommended[:k]
    relevant_set=set(relevant)
    hits_k=[x for x in top_k if x in relevant_set]
    precision=len(hits_k)/k
    recall=len(hits_k)/len(relevant)
    return [precision,recall]
    