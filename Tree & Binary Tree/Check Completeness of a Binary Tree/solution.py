# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    while q and q[-1] is None: q.pop()
                    if q: return False
                    return True
                q.append(node.left)
                q.append(node.right)
        return True
