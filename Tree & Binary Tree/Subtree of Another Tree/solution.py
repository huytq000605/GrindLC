# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(tree, sub):
            if not sub and not tree:
                return True
            if not tree or not sub:
                return False
            if tree.val == sub.val:
                if dfs(tree.left, sub.left) and dfs(tree.right, sub.right):
                    return True
            if sub != subRoot:
                return False
            return dfs(tree.left, sub) or dfs(tree.right, sub)
        return dfs(root, subRoot)
