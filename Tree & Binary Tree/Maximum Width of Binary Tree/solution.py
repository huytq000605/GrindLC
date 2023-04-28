# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        result = 0
        while q:
            mn = math.inf
            for _ in range(len(q)):
                u, level = q.popleft()
                mn = min(mn, level)
                result = max(result, level - mn)
                if u.left: q.append((u.left, level * 2 + 1))
                if u.right: q.append((u.right, level * 2 + 2))
        return result + 1
            
