# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q: return 0
        result = -1
        def dfs(u):
            nonlocal result
            if not u: return 0, False
            l, lv = dfs(u.left)
            r, rv = dfs(u.right)
            # u is LCA of p and q
            if lv and rv: 
                result = l + r + 2
                return 0, False
            if u.val in [p, q]:
                if lv or rv: 
                    result = l + r + 1
                    return 0, False
                return 0, True
            if lv or rv:
                return l+r+1, True
            return 0, False
        dfs(root)
        return result

            
