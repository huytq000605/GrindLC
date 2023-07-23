# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            result = []
            for i in range(1, n):
                lefts = self.allPossibleFBT(i)
                rights = self.allPossibleFBT(n-1-i)
                for left in lefts:
                    for right in rights:
                        node = TreeNode(0, left, right)
                        result.append(node)
            return result
        return dfs(n)
