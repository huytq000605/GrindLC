# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        result = []
        s = 0
        def dfs(node):
            nonlocal path, result, s
            if not node:
                return
            path.append(node.val)
            s += node.val
            if not node.left and not node.right and s == targetSum:
                result.append([*path])
            dfs(node.left)
            dfs(node.right)
            path.pop()
            s -= node.val
        dfs(root)
        return result
        
