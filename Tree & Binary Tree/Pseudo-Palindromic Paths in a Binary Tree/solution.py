# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq = [0 for _ in range(10)]
        result = 0

        def pseudo_palindrome(freq):
            odd = 0
            for v in freq:
                if v % 2 == 1:
                    odd += 1
                if odd > 1:
                    return False
            return True

        def dfs(u):
            nonlocal result, freq
            freq[u.val] += 1
            if not u.left and not u.right:
                result += pseudo_palindrome(freq)
            if u.left:
                dfs(u.left)
            if u.right:
                dfs(u.right)
            freq[u.val] -= 1
        
        dfs(root)
        return result#         self.right = right
