"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = dict()
        def build(node):
            if node in mapping:
                return mapping[node]
            if not node:
                return None
            root = Node(node.val)
            mapping[node] = root
            if node.neighbors:
                root.neighbors = []
                for adj in node.neighbors:
                    root.neighbors.append(build(adj))
            return root
        return build(node)