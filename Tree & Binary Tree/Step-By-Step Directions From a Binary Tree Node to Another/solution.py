# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        node1 = None
        node2 = None
        parents = dict()
        
        def findNode(node, prev):
            nonlocal node1, node2, parents
            if not node:
                return
            if node.val == startValue:
                node1 = node
            if node.val == destValue:
                node2 = node
            if prev:
                parents[node] = prev
            findNode(node.left, node)
            findNode(node.right, node)
        
        findNode(root, None)
        def findLCA(node):
            if not node:
                return None
            if node == node1 or node == node2:
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if not left:
                return right
            if not right:
                return left
            if left and right:
                return node
            
        lca = findLCA(root)
        result = ""
        current = node1
        while current != lca:
            result += "U"
            current = parents[current]
        
        current = node2
        prev = None
        path2 = ""
        while current != lca:
            prev = current
            current = parents[current]
            if current.left == prev:
                path2 += "L"
            else:
                path2 += "R"
        result += path2[::-1]
        return result