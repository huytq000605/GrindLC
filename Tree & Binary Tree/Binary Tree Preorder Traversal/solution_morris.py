# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        result = []
        while current:
            result.append(current.val)
            if not current.left:
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != current and predecessor.right:
                    predecessor = predecessor.right

                if predecessor.right == None:
                    predecessor.right = current.right
                    current = current.left
                else:
                    current = current.right
        return result
