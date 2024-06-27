
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        stack = []
        result = -1
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if result == -1 or abs(target - node.val) < abs(target - result):
                result = node.val
            node = node.right
        return result


