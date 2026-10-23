# Understanding Go Groups and Liberties

Before a program can decide whether a Go move is legal or whether stones should be captured, it needs a precise way to answer two basic questions: which stones belong together, and where can that group still breathe? This problem builds exactly that foundation.

## Stones live as groups

A Go board is a grid of intersections. In this representation, Black stones use the value 1, White stones use the value -1, and empty intersections use 0. A single stone can be part of a larger group when it touches another stone of the same colour vertically or horizontally.

The important word is connected. Two same-colour stones belong to one group when there is a path of same-colour stones between them using only the four orthogonal directions:

- one row above,
- one row below,
- one column to the left,
- one column to the right.

Diagonal contact does not connect stones in Go. If two Black stones touch only at their corners, they are separate groups and must be examined separately.

Thinking in groups matters because capture is decided for the whole connected group. A stone that appears surrounded may still be safe because another stone in its group reaches an empty intersection elsewhere.

## What a liberty means

A liberty is an empty intersection directly beside at least one stone in the group. Like connectivity, adjacency is only vertical or horizontal. The edge of the board is not a liberty because it is not an intersection, and an opposing stone is not a liberty because it is occupied.

Several stones may touch the same empty point. That point still counts as one liberty, not several. This is why the result asks for distinct liberty coordinates. The question is about how many available intersections the group has, rather than how many stone-to-empty contacts exist.

For an L-shaped group at (0, 0), (0, 1), and (1, 1), an empty point at (1, 0) touches two stones in the group. It is still one liberty.

## Exploring the entire connected group

The starting row and column identify one occupied point. From that point, the group can be found by a graph traversal. You can imagine each same-colour stone as a node and each orthogonal connection as an edge.

A frontier, represented by a stack or queue, stores stones that have been discovered but not fully examined. A visited collection records stones already known to belong to the group. For every stone removed from the frontier, inspect its four possible neighbours.

Each valid neighbour has one of three meanings:

- An empty neighbour is added to the liberty collection.
- A same-colour neighbour belongs to the group and should be explored if it has not been visited.
- An opposing stone blocks that direction and is ignored for this task.

The traversal finishes when the frontier is empty. At that point, every stone reachable from the starting point has been found. This works for straight chains, branching shapes, loops, and groups that run along an edge or into a corner.

## Why visited collections are necessary

Connected stones can lead back to one another. Without a visited check, the traversal can repeatedly move between the same points. A loop-shaped group makes the issue especially clear: following neighbours eventually returns to a stone that was already seen.

A set is a natural choice for both groups and liberties because membership checks are direct and duplicate insertions do not change the result. The group set prevents repeated traversal, while the liberty set prevents shared empty intersections from being counted more than once.

There is a useful invariant throughout the search: every coordinate in the group collection contains the starting colour, and every coordinate in the liberty collection is empty and touches at least one discovered group stone. Preserving these facts makes the final result trustworthy.

## Board boundaries

Every neighbour coordinate must be checked before reading the board. A corner stone has only two possible board neighbours, an edge stone has three, and an interior stone has four. Moving above the top row or left of the first column does not create a liberty; it simply leaves the board.

This detail also prevents a subtle NumPy problem. Negative indices are valid in NumPy and refer to positions counted from the end. If an unchecked neighbour of the top row uses row -1, the program may accidentally inspect the bottom row instead of rejecting the coordinate. Explicit boundary checks are therefore part of the game logic, not merely defensive programming.

## Deterministic output

Sets do not promise the row-column order required by the problem. After the search is complete, both coordinate collections must be sorted lexicographically. This means rows are compared first, followed by columns when two coordinates share a row.

Sorting has no effect on which stones or liberties were discovered. It gives the same representation every time, which makes examples, tests, and later game logic easier to compare.

The board itself should remain unchanged. This function is inspecting a position, not playing a move. Converting the input to a NumPy view for reading is fine, but writing stones or markers into that array would mix traversal state with game state and could mutate the caller's board.

## Common mistakes to avoid

- Treating diagonals as connections joins groups that are separate under Go rules.
- Counting the same liberty once per adjacent stone overstates the group's breathing space.
- Marking points by changing the board violates the requirement to preserve the input.
- Forgetting boundary checks can make opposite edges appear connected through negative indexing.
- Returning an unordered set produces unstable output even when the discovered points are correct.

The central idea is simple: start from one stone, follow every orthogonal path through stones of the same colour, and collect the distinct empty intersections touching that connected component. This group-and-liberty operation will later support capture detection, suicide checks, and legal move generation.

---