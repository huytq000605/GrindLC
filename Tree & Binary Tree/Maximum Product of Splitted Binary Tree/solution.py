# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node:
                return 0
            return node.val + dfs(node.left) + dfs(node.right)
        
        result = 0
        s = dfs(root)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result = max(result, (s - dfs(node)) * dfs(node) )
        return result % (10**9 + 7)
