from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = dict()

        def dfs(node, row, col):
            if node == None:
                return
            if col not in cols:
                cols[col] = []
            cols[col].append([row, node.val])
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1,col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(list(cols.keys())):
            nodes = [node for row, node in sorted(cols[col])]
            
            result.append(nodes)
            
        return result
        