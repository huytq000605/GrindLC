# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        q = [root]
        while q:
            nq = []
            s = 0
            while q:
                node = q.pop()
                if node.left: nq.append(node.left)
                if node.right: nq.append(node.right)
                s += node.val
            q = nq
            heappush(pq, s)
            if len(pq) > k:
                heappop(pq)
        if len(pq) < k:
            return -1
        return pq[0]
