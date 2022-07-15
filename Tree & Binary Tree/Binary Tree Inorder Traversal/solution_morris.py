# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        result = []
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != current and predecessor.right:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    predecessor.right = current
                    current = current.left
                else:
                    result.append(current.val)
                    current = current.right
        return result
