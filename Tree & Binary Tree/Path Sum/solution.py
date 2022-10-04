# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        s = 0
        def dfs(node):
            nonlocal s
            if not node:
                return False
            s += node.val
            if not node.left and not node.right and s == targetSum:
                return True
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            s -= node.val
            return False
        return dfs(root)
            
                
