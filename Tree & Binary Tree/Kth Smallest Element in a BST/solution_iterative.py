# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while (node or stack) and k:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
        return node.val
            