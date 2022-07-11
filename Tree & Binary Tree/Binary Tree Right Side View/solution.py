# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        result = [root.val]
        while q:
            nq = deque()
            while q:
                node = q.popleft()
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            if nq:
                result.append(nq[-1].val)
            q = nq
        return result
