# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start, end):
            if start > end:
                return [None]
            result = []
            for mid in range(start, end+1):
                lefts = build(start, mid-1)
                rights = build(mid+1, end)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(mid, left, right)
                        result.append(root)
            return result
        return build(1, n)
