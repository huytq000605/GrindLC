# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node):
            nonlocal key
            if not node:
                return
            if node.val == key:
                left = node.left
                right = node.right
                if not left or not right:
                    return left or right
                replace = right
                while right.left:
                    right = right.left
                right.left = left
                return replace
            else:
                if node.val > key:
                    node.left = dfs(node.left)
                else:
                    node.right = dfs(node.right)
                return node
        return dfs(root)