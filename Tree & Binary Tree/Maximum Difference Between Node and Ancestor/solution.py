# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, mn, mx):
            nonlocal result
            if not node: return
            result = max(result, node.val - mn, mx - node.val)
            dfs(node.left, min(mn, node.val), max(mx, node.val))
            dfs(node.right, min(mn, node.val), max(mx, node.val))
        dfs(root, root.val, root.val)
        return result
        
