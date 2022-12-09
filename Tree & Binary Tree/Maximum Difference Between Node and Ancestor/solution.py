# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, mx, mn):
            if not node:
                return
            nonlocal result
            result = max(result, abs(mx - node.val), abs(mn - node.val))
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            dfs(node.left, mx, mn)
            dfs(node.right, mx, mn)
        dfs(root, root.val, root.val)
        return result
