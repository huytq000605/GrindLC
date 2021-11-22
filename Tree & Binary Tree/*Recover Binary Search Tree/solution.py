# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        wrong1 = None
        wrong2 = None
        prevNode = TreeNode(-math.inf)
        
        def dfs(node):
            nonlocal wrong1
            nonlocal wrong2
            nonlocal prevNode
            if node == None:
                return
            dfs(node.left)
            
            if wrong1 == None and node.val < prevNode.val: # first time find wrong node
                wrong1 = prevNode
            if wrong1 != None and node.val < wrong1.val: # keep finding last wrong node
                wrong2 = node
            
            prevNode = node
            dfs(node.right)
        
        dfs(root)
        wrong1.val, wrong2.val = wrong2.val, wrong1.val
        return root
            
            
        