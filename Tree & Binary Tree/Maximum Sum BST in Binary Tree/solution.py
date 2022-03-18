# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                return True, -math.inf, math.inf, 0
            
            if not node.left and not node.right:
                result = max(result, node.val)
                return True, node.val, node.val, node.val
            
            left_is_BST, left_max_value, left_min_value, left_total = dfs(node.left)
            right_is_BST, right_max_value, right_min_value, right_total = dfs(node.right)
            
            if not node.left:
                if right_is_BST and node.val < right_min_value:
                    result = max(result, right_total + node.val)
                    return True, right_max_value, node.val, right_total + node.val
            
            if not node.right:
                if left_is_BST and node.val > left_max_value:
                    result = max(result, left_total + node.val)
                    return True, node.val, left_min_value, left_total + node.val
            
            if left_is_BST and right_is_BST and left_max_value < node.val and right_min_value > node.val:
                result = max(result, left_total + right_total + node.val)
                return True, right_max_value, left_min_value, left_total + right_total + node.val
            
            return False, math.inf, -math.inf, node.val
        
        dfs(root)
        return result