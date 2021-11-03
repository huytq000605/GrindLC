# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = 0
        def getNum(node: TreeNode, current: int):
            if node == None:
                return
            current += node.val
            if node.left == None and node.right == None:
                result += current
                return
            getNum(node.left, current)
            getNum(node.right, current)
        
        getNum(root, 0)
        return result
        
                
        
        