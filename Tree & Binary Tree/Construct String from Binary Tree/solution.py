# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        def dfs(u):
            nonlocal result
            if not u:
                return
            result += "("
            result += str(u.val)
            left = dfs(u.left)
            if not u.left and u.right:
                result += "()"
            right = dfs(u.right)
            result += ")"
        dfs(root)
        return result[1:-1]
               



