from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(maxsize=None)
        def cal(node: TreeNode, prevRob: bool):
            if node == None:
                return 0
            if prevRob:
                return cal(node.left, False) + cal(node.right, False)
            else:
                robThis = node.val + cal(node.left, True) + cal(node.right, True)
                passThis = cal(node.left, False) + cal(node.right, False)
                return max(robThis, passThis)
        return cal(root, False)