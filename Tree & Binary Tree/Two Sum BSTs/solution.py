# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        s1, s2 = [], []
        while True:
            while root1:
                s1.append(root1)
                root1 = root1.left
            while root2:
                s2.append(root2)
                root2 = root2.right
            if not s1 or not s2:
                break
            n1, n2 = s1.pop(), s2.pop()
            if n1.val + n2.val == target:
                return True

            if n1.val + n2.val > target:
                s1.append(n1)
                root2 = n2.left
            else:
                s2.append(n2)
                root1 = n1.right
        return False
