# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prefix = 0
        def dfs(node):
            nonlocal prefix
            if not node: return
            dfs(node.right)
            prefix += node.val
            node.val = prefix
            dfs(node.left)
        dfs(root)
        return root
