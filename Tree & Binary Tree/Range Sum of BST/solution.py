# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            result = 0
            if node.val >= low and node.val <= high:
                result += node.val
                result += dfs(node.left)
                result += dfs(node.right)
            elif node.val < low:
                result += dfs(node.right)
            elif node.val > high:
                result += dfs(node.left)
            return result
        return dfs(root)