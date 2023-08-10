# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        have_q, have_p = False, False
        def dfs(u):
            nonlocal have_q, have_p
            if not u:
                return None
            left = dfs(u.left)
            right = dfs(u.right)
            if u == p:
                have_p = True
                return u
            if u == q:
                have_q = True
                return u
            if left and right:
                return u
            if left: return left
            if right: return right
            return None
        u = dfs(root)
        if have_q and have_p: return u
        return None

            
