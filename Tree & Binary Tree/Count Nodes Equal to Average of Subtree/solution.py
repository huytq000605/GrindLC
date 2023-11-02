# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(u):
            nonlocal result
            if not u:
                return 0, 0
            s = u.val
            n = 1
            s_left, n_left = dfs(u.left)
            s_right, n_right = dfs(u.right)
            s += s_left + s_right
            n += n_left + n_right
            if s // n == u.val:
                result += 1
            return s, n
        dfs(root)
        return result
            
