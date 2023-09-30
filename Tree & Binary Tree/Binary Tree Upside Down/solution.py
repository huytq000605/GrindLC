# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return None
            result = node
            if node.left:
                result = dfs(node.left)
                node.left.left = node.right
                node.left.right = node
                node.left = None
                node.right = None
            return result
        return dfs(root)
