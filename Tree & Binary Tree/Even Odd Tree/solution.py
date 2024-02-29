# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        dq = deque([root])
        while dq:
            prev = 0
            for _ in range(len(dq)):
                u = dq.popleft()
                if level & 1 == u.val & 1: return False
                if level & 1 and prev != 0 and prev <= u.val: return False
                if not level & 1 and prev >= u.val: return False
                prev = u.val
                if u.left: dq.append(u.left)
                if u.right: dq.append(u.right)
            level += 1
        return True
