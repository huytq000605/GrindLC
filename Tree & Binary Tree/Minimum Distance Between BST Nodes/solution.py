# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -1
        result = math.inf
        def dfs(u):
            nonlocal result, prev
            if u.left: dfs(u.left)
            if prev != -1: result = min(result, u.val - prev)
            prev = u.val
            if u.right: dfs(u.right)
        dfs(root)
        return result
