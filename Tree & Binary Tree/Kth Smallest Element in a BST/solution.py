# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return
            left = dfs(node.left)
            if k == 0:
                return left
            k -= 1
            if k == 0:
                return node
            return dfs(node.right)
        return dfs(root).val
            