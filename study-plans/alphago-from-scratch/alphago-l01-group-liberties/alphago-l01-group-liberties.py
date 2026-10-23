import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """
    arr = np.array(board)
    rows, cols = arr.shape
    color = arr[row, col]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Step 1: flood fill to find the connected same-color group
    group = []
    visited = set()
    stack = [(row, col)]
    visited.add((row, col))

    while stack:
        r, c = stack.pop()
        group.append((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and arr[nr, nc] == color:
                    visited.add((nr, nc))
                    stack.append((nr, nc))

    # Step 2: collect unique empty neighbors = liberties
    liberties = set()
    for r, c in group:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if arr[nr, nc] == 0:
                    liberties.add((nr, nc))

    # Step 3: sort by row then column and return
    return (sorted(group), sorted(liberties))