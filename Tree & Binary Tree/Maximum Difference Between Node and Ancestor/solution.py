# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, max_value, min_value):
            nonlocal result
            if not node:
                return
            result = max(result, abs(max_value - node.val), abs(min_value - node.val))
            max_value = max(max_value, node.val)
            min_value = min(min_value, node.val)
            dfs(node.left, max_value, min_value)
            dfs(node.right, max_value, min_value)
        if not root:
            return 0
        dfs(root, root.val, root.val)
        return result
            
