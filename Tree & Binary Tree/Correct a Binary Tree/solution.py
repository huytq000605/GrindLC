# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        dq = deque([(root, None)])
        seen = set()
        while dq:
            u, p = dq.popleft()
            seen.add(u)
            if u.right in seen:
                if p.left == u:
                    p.left = None
                if p.right == u:
                    p.right = None
                return root
            if u.right:
                dq.append((u.right, u))
            if u.left:
                dq.append((u.left, u))
            
        return root
