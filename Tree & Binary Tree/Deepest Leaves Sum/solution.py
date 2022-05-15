# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def find_max_level(node):
            if not node:
                return 0
            return 1 + max(find_max_level(node.left), find_max_level(node.right))
        max_level = find_max_level(root)
        def dfs(node, level):
            nonlocal max_level
            if not node:
                return 0
            if level == max_level:
                return node.val
            return dfs(node.left, level + 1) + dfs(node.right, level + 1)
        return dfs(root, 1)
    