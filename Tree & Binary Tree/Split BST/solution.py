# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def dfs(node):
            result = [None, None]
            if not node: return result
            if node.val > target:
                result[1] = node
                split_tree, keep_tree = dfs(node.left)
                node.left = keep_tree
                result[0] = split_tree
            else:
                result[0] = node
                split_tree, keep_tree = dfs(node.right)
                node.right = split_tree
                result[1] = keep_tree     
            return result
        return dfs(root)

