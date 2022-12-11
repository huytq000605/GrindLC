# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -math.inf
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            cur = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            result = max(result, cur + left, cur + right, cur, cur + left + right)
            return max(cur + left, cur, cur + right)
        dfs(root)
        return result
