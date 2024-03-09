
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                u = dq.pop()
                if u.right: dq.appendleft(u.right)
                if u.left: dq.appendleft(u.left)
                result = u
        return result.val
            

