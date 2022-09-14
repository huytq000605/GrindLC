# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = [0 for i in range(10)]
        result = 0
        def dfs(node):
            if not node:
                return
            nonlocal result
            count[node.val] += 1
            if not node.left and not node.right:
                count_odd = 0
                for i in range(10):
                    if count[i] % 2 == 1:
                        count_odd += 1
                if count_odd <= 1:
                    result += 1
            dfs(node.left)
            dfs(node.right)
            count[node.val] -= 1
        dfs(root)
        return result
                
                            
