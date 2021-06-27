from typing import Dict

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.connected = []
        self.isLeaf = False

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def buildGraph(node: TreeNode, leafNodes, parent = None):
            result = GraphNode(node.val)
            if node.left == None and node.right == None:
                result.isLeaf = True
                leafNodes.append(result)
            if parent != None:
                result.connected.append(parent)
            if node.left != None:
                result.connected.append(buildGraph(node.left, leafNodes, result))
            if node.right != None:
                result.connected.append(buildGraph(node.right, leafNodes, result))
            return result
        
        def dfs(node: GraphNode, distance: int, seen: Dict, starting = False):
            if distance < 0 :
                return 0
            if seen.get(node) != None:
                return 0
            seen[node] = True
            if node.isLeaf and starting == False:
                return 1
            result = 0
            for connect in node.connected:
                result += dfs(connect, distance - 1, seen)
            return result
        
        result = 0
        leafNodes = []
        buildGraph(root, leafNodes, None)
        for leafNode in leafNodes:
            seen = {}
            result += dfs(leafNode, distance, seen, True)
        return int(result/2)