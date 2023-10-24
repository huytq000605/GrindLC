# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = [root]
        while q:
            nq = []
            mx = q[0].val
            while q:
                u = q.pop()
                if u.left:
                    nq.append(u.left)
                if u.right:
                    nq.append(u.right)
                mx = max(mx, u.val)
            q = nq
            result.append(mx)
        return result
