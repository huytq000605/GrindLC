"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        mapping = [None for _ in range(101)]
        def dfs(node):
            if mapping[node.val]: return mapping[node.val]
            clone_node = Node(node.val, [])
            mapping[node.val] = clone_node
            if node.neighbors:
                clone_node.neighbors = []
                for v in node.neighbors:
                    clone_node.neighbors.append(dfs(v))
            return clone_node
        return dfs(node)
