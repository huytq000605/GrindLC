# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        max_value = -math.inf
        result = 0
        level = 1
        while dq:
            value = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                value += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if value > max_value:
                max_value = value
                result = level
            level += 1
        return result
