# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        nq = deque()
        level = 0
        while q:
            if level % 2 == 1:
                i, j = 0, len(q) - 1
                while i < j:
                    q[i].val, q[j].val = q[j].val, q[i].val
                    i += 1
                    j -= 1
            while q:
                node = q.popleft()
                if node.left:
                    nq.append(node.left)
                    nq.append(node.right)
            q, nq = nq, q
            level += 1    
        return root
