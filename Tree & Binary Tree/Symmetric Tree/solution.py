# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(u, v):
            if not u and not v:
                return True
            if not u or not v:
                return False
            if u.val != v.val:
                return False
            return dfs(u.left, v.right) and dfs(u.right, v.left)
        return dfs(root.left, root.right)
            
