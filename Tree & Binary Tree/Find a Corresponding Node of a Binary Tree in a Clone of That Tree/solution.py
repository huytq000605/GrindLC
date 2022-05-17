# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s1, s2 = [original], [cloned]
        
        def add_node(node, stack):
            if node.left:
                stack.append(node.left)
            if node.right:    
                stack.append(node.right)
                
        while s1 and s2:
            n1, n2 = s1.pop(), s2.pop()
            if n1 == target:
                return n2
            add_node(n1, s1)
            add_node(n2, s2)
        
        return None