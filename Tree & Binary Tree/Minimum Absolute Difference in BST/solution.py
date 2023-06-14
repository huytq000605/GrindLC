# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = math.inf
        prev = -math.inf
        def dfs(node):
            nonlocal result, prev
            if node.left: dfs(node.left)
            result = min(result, node.val - prev)
            prev = node.val
            if node.right: dfs(node.right)
        dfs(root)
        return result
            
