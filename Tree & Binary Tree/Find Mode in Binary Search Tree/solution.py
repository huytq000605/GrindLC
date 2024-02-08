# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        freq = 0
        val = -1
        mx_freq = 0
        def dfs(u):
            nonlocal result, freq, val, mx_freq
            if not u:
                return
            dfs(u.left)
            if u.val != val:
                val = u.val
                freq = 0
            freq += 1
            if freq > mx_freq:
                mx_freq = freq
                result = [u.val]
            elif freq == mx_freq:
                result.append(u.val)
            dfs(u.right)
            return
        dfs(root)
        return result
