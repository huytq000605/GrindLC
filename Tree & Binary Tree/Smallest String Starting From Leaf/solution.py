
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = ""
        offset = ord('a')
        def dfs(node, s):
            nonlocal result
            s += chr(node.val + offset)
            if not node.left and not node.right:
                s = s[::-1]
                if not result or s < result:
                    result = s
                return
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
        dfs(root, "")
        return result
