# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        result = 0
        def dfs(u):
            nonlocal result
            if not u:
                return 0, 0
            l, lc = dfs(u.left)
            r, rc = dfs(u.right)
            s = l + r + u.val
            n = lc + rc + 1
            result = max(result, s / n)
            return s, n
        dfs(root)
        return result
        
