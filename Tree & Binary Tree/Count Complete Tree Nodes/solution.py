# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if not node:
            return 0
        return 1 + self.height(node.left)
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = self.height(root.left), self.height(root.right)
        if left > right:
            return self.countNodes(root.left) + (1 << right)
        else:
            return (1 << left) + self.countNodes(root.right)
        
        
        
