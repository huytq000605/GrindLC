# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        result = []
        def dfs(node):
            left = ""
            right = ""
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            cur = f"{node.val}#{left}#{right}"
            if seen[cur] == 1:
                result.append(node)
            seen[cur] += 1
            return cur
        dfs(root)
        return result
