# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            if (left_sum + right_sum + node.val) // (left_count + right_count + 1) == node.val:
                result += 1
            return left_sum + right_sum + node.val, left_count + right_count + 1
        dfs(root)
        return result