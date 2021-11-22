# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == key:
            if root.left == None:
                root = root.right
                return root
            if root.right == None:
                root = root.left
                return root
            
            replace = root.right
            while replace.left != None:
                replace = replace.left
            root.val = replace.val
            root.right = self.deleteNode(root.right, replace.val)
        else:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                root.left = self.deleteNode(root.left, key)
        return root