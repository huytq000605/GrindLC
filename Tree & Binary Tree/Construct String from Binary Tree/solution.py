# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = ""
        def dfs(node):
            nonlocal result
            result += "("
            if node:
                result += str(node.val)
                if node.left or node.right:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            result += ")"
        dfs(root)
        return result[1:-1]
