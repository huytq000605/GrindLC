# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        numbers = []
        def getNum(node: TreeNode, current: str):
            if node == None:
                return
            current += str(node.val)
            if node.left == None and node.right == None:
                numbers.append(int(current))
                return
            getNum(node.left, current)
            getNum(node.right, current)
        
        getNum(root, "")
        sum = 0
        for num in numbers:
            sum += num
        return sum
        
                
        
        