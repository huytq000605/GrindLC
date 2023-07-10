# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        s = 1
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if not node.left and not node.right:
                    return s
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            s += 1
        return s
             
