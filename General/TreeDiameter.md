# Tree Diameter

## To find maximum distance between any 2 nodes in in tree

- **DFS way**

We have a global variable furthest = [fursthestNode, fursthestLength]

Choose a random node to be startingPoint

First, we define a function call dfs(node, parent, length) which dfs through the tree and modify furthest if length > furthest[1]

Run dfs(startingPoint, -1, 0)

After dfs, we got furthest node from starting point, we assign new startingPoint = this furthest node. Then we find furthest node from new startingPoint by dfs(newStartingPoint, -1, 0)

After seconf dfs, the furthest distance is diameter of the tree


- **BFS Way**
  
Each node in the queue will be [node, distance]

Random start BFS

First time BFS => find first furthest node

BFS 2nd time from the node we've found

=> Found furthest node from new starting point, and their distance will be diameter of the tree