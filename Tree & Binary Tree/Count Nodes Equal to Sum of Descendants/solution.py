# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(u):
            if not u:
                return 0, 0
            s1, n1 = dfs(u.left)
            s2, n2 = dfs(u.right)
            return s1 + s2 + u.val, n1 + n2 + ((s1 + s2) == u.val)
            
        return dfs(root)[1]
