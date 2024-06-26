# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vs = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            vs.append(root.val)
            root = root.right
        
        def build(l, r):
            if l > r: return None
            mid = l + (r - l) // 2
            return TreeNode(vs[mid], build(l, mid-1), build(mid+1, r))
        
        return build(0, len(vs) - 1)

        
