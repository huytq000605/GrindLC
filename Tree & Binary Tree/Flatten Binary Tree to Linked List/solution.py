# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        tail_left = self.flatten(root.left)
        tail_right = self.flatten(root.right)
        if root.left:
            tail_left.right = root.right
            root.right = root.left
            root.left = None
        # return to the deepest node from this node
        return tail_right or tail_left or root
