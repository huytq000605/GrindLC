# Tree / Graph Diameter

**Idea:** The **diameter** is the maximum distance between any two nodes. There are two classic ways to compute it: a single DFS that combines the two longest child paths at each node, or two passes of DFS/BFS (find the farthest node from anywhere, then the farthest node from *that* node).

## DFS Combining Two Longest Child Paths

Find the maximum distance between any two nodes in a tree with one post-order traversal.

- Keep a global variable `diameter`.
- Do a post-order traversal; each DFS call returns the longest path from the node down to a child.
- During a DFS call:
    - Keep `longest_path` = the longest path from this node to a child, initialized to `0`.
    - Loop through each child `v` (with parent `u`):
        - `dfs(v, u) = path`
        - `diameter = max(diameter, longest_path + path)`
        - `longest_path = max(longest_path, path)`
    - Return `longest_path + 1`.
- Return `diameter`.

## Two-Pass DFS / BFS

Find the maximum distance between any two nodes by walking the tree twice.

**DFS way**

- Keep a global variable `furthest = [furthestNode, furthestLength]`.
- Choose a random node as `startingPoint`.
- Define `dfs(node, parent, length)` that traverses the tree and updates `furthest` whenever `length > furthest[1]`.
- Run `dfs(startingPoint, -1, 0)`.
- After this DFS we have the farthest node from the start. Set the new `startingPoint` to that node, then run `dfs(newStartingPoint, -1, 0)` again.
- After the second DFS, `furthest` distance is the diameter of the tree.

**BFS way**

- Each queue entry is `[node, distance]`.
- Start BFS from a random node — the first BFS finds the first farthest node.
- Run BFS a second time from the node we found.
- The farthest distance from this new starting point is the diameter of the tree.

## Relation to Minimum Tree Height (We Can Choose the Root)

- If the diameter is `d`, the minimum possible height is `(d + 1) // 2`.
- To achieve it, choose the **center node** of the diameter path as the root. Any other choice fails to balance the paths to all nodes, so `max(path) > (d + 1) // 2`.
