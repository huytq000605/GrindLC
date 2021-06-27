# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def findXNode(node: TreeNode) -> TreeNode:
            if node == None: return None
            if node.val == x:
                return node
            find_left = findXNode(node.left)
            if find_left != None: return find_left
            find_right = findXNode(node.right)
            return find_right
        
        def countNode(node: TreeNode) -> int:
            if node == None: return 0
            return 1 + countNode(node.left) + countNode(node.right)
        
        xNode = findXNode(root)
        count_left = countNode(xNode.left)
        count_right = countNode(xNode.right)
        if count_left + count_right + 1 < n / 2 or count_left > n/2 or count_right > n/2:
            return True
        return False