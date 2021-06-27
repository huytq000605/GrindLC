from typing import Dict, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def buildParentMap(node: TreeNode, parentMap: Dict[TreeNode, TreeNode]):
            if node.left != None:
                parentMap[node.left] = node
                buildParentMap(node.left, parentMap)
            if node.right != None:
                parentMap[node.right] = node
                buildParentMap(node.right, parentMap)
        
        def dfs(node: TreeNode, distance: int, seen: Dict[TreeNode, bool], starting = False):
            nonlocal parentMap
            if node == None:
                return 0
            if distance < 0 :
                return 0
            if seen.get(node) != None:
                return 0
            seen[node] = True
            if node.left == None and node.right == None and starting == False:
                return 1
            # parent = parentMap[node]
            
            return dfs(node.left, distance - 1, seen) + dfs(node.right, distance - 1, seen) + dfs(parentMap.get(node), distance - 1, seen)
        
        def getLeafNodes(node: TreeNode, leafNodes: List[TreeNode] = []) -> List[TreeNode]:
            if node == None:
                return leafNodes
            if node.left == None and node.right == None:
                leafNodes.append(node)
                return leafNodes
            getLeafNodes(node.left, leafNodes)
            getLeafNodes(node.right, leafNodes)
            return leafNodes
            
        
        result = 0
        leafNodes = getLeafNodes(root)
        parentMap = {}
        buildParentMap(root, parentMap)
        for leafNode in leafNodes:
            seen = {}
            result += dfs(leafNode, distance, seen, True)
        return int(result/2)