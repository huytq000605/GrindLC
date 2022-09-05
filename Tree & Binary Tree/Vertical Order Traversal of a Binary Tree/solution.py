# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        min_col, max_col = 0, 0
        def dfs(node, row, col):
            nonlocal min_col, max_col
            if not node:
                return
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append([row, node.val])
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root, 0, 0)
        result = []
        for col in range(min_col, max_col + 1):
            result.append(([val for row, val in sorted(cols[col])]))
        return result
