# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node, go_left, current):
            nonlocal result
            if not node: return 0
            result = max(result, current)
            if go_left: 
                dfs(node.left, False, current + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, current + 1)
                dfs(node.left, False, 1)
        dfs(root, True, 0)
        return result
        
