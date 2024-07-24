# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        stack = [root]
        result = []
        if root.val not in to_delete:
            result.append(root)
        while stack:
            u = stack.pop()
            if u.left: stack.append(u.left)
            if u.right: stack.append(u.right)

            if u.val in to_delete:
                if u.left and u.left.val not in to_delete:
                    result.append(u.left)
                if u.right and u.right.val not in to_delete:
                    result.append(u.right)
            else:
                if u.left and u.left.val in to_delete:
                    u.left = None
                if u.right and u.right.val in to_delete:
                    u.right = None

            
        return result
            
