# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1, s2 = [root1], [root2]

        def dfs(s):
            while s:
                cur = s.pop()
                if cur.right:
                    s.append(cur.right)
                if cur.left:
                    s.append(cur.left)
                if not cur.left and not cur.right:
                    return cur.val
        while s1 and s2:
            if dfs(s1) != dfs(s2):
                return False
        return not s1 and not s2
