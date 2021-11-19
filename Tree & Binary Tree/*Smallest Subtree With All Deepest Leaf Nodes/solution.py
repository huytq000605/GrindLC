# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node == None:
                return None, 0
            left, leftLevel = dfs(node.left)
            right, rightLevel = dfs(node.right)
            if leftLevel < rightLevel:
                return right, rightLevel + 1
            elif leftLevel > rightLevel:
                return left, leftLevel + 1
            else:
                return node, leftLevel + 1
        dfs(root)
        return dfs(root)[0]