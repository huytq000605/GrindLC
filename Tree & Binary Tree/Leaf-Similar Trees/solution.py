# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node:
                return
            dfs(node.left, arr)
            if not node.left and not node.right:
                arr.append(node.val)     
            dfs(node.right, arr)
        
        arr1 = []
        dfs(root1, arr1)
        idx = 0
        
        def dfs2(node):
            nonlocal idx, arr1
            if not node:
                return True
            if not dfs2(node.left):
                return False
            if not node.left and not node.right:
                if idx >= len(arr1) or arr1[idx] != node.val:
                    return False
                idx += 1
                return True
            if not dfs2(node.right):
                return False
            return True
        
        return dfs2(root2) and idx == len(arr1)