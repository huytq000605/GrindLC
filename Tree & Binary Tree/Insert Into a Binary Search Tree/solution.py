# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, parent, left = True):
            nonlocal root
            if not node:
                if not root:
                    root = TreeNode(val)
                else:
                    if left:
                        parent.left = TreeNode(val)
                    else:
                        parent.right = TreeNode(val)
                return
            if val > node.val:
                dfs(node.right, node, False)
            else:
                dfs(node.left, node, True)
        
        dfs(root, None, True)
        return root
