# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root, 0)])
        while q:
            nq = deque()
            s = sum(u.val for u, v in q)
            while q:
                u, v = q.popleft()
                u.val = s - u.val - v
                if u.left:
                    v = 0
                    if u.right: v = u.right.val
                    nq.append((u.left, v))
                if u.right:
                    v = 0
                    if u.left: v = u.left.val
                    nq.append((u.right, v))
            q = nq
        return root
                
                
