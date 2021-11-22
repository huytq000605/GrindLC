# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 1
        def dfs(node):
            nonlocal result
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            length = 1
            returnValue = 1
            if node.left and node.left.val == node.val:
                length += left
                returnValue = max(returnValue, 1 + left)
            if node.right and node.right.val == node.val:
                length += right
                returnValue = max(returnValue, 1 + right)
            result = max(result, length)
            return returnValue
        dfs(root)
        return result - 1
            