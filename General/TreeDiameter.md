# Tree Diameter
## To find maximum distance between any 2 nodes in in a graph
- Keep track global variable diameter
- Do post order traversal, each dfs call returns the longest path from parent to child.
- During DFS call
    - Keep track of the longest path from node to a child, called it longest_path, init to be 0
    - During the loop through each child
        - dfs(v, u) = path
        - diamater = max(diamater, longest_path + path)
        - longest_path = max(longest_path, path)
    - Return longest_path + 1
- Return diamater

## Relation between minimum height of the trees (We can choose the root):
- Diameter is d, so the shorest tree would be (d+1)//2
- If we want to find the tree, need to choose the center node in diameter path as the root. If we choose another node, it shows that it doesn't balance out the path to all nodes so max(path) > (d+1)//2



# Graph Diameter

## To find maximum distance between any 2 nodes in in a graph

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
