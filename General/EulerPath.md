# Euler Path

## Problems:
1. 2097: Valid Arrangement of Pairs Valid Arrangement of Pairs
2. 332: Reconstruct Itinerary

- countFrom[i] and countTo[i] to count how many edges come from and to node i

- A graph has euler path if and only if
	1. countFrom[i] == countTo[i] for all nodes
	2. countFrom[i] == countTo[i] for all nodes except exactly 2 nodes, 1 have countFrom[i] - countTo[i] == 1 and the other has countTo[i] - countFrom[i] == 1

- In first case: all Euler path is Euler circuits, starting point can be any node
- In second case, starting point of euler path must be the node have countFrom[i] - countTo[i] == 1

- Algorithm: We use post order to traverse from the start, append the path from end to start (using stack then reverse or use deque). The key is if we go to a true path, then just like normal dfs, if we go wrong, because of postorder, so we will comeback to the wrong node and merge right path before wrong path => true path
