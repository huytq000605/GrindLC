# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        result = 0
        # If not infected, return the depth of the subtree
        # If it's infected, return the depth from the infected node
        def dfs(node):
            nonlocal result
            if not node:
                return 0, False  
            left, left_infected = dfs(node.left)
            right, right_infected = dfs(node.right)

            if node.val == start:
                result = max(result, left, right)
                return 0, True
            elif left_infected:
                result = max(result, left + right + 1)
                return left + 1, True
            elif right_infected:
                result = max(result, left + right + 1)
                return right + 1, True
            else:
                result = max(result, max(left, right) + 1)
                return max(left, right) + 1, False
        dfs(root)
        return result
