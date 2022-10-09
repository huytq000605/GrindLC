# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack_left, stack_right = [], []
        
        def push_left(node):
            while node:
                stack_left.append(node)
                node = node.left
            
        def next_left():
            res = stack_left.pop()
            push_left(res.right)
            return res
        
        def push_right(node):
            while node:
                stack_right.append(node)
                node = node.right
        
        def next_right():
            res = stack_right.pop()
            push_right(res.left)
            return res
        
        push_left(root)
        push_right(root)
        left, right = next_left(), next_right()
        while left.val < right.val:
            s = left.val + right.val
            if s == k:
                return True
            elif s < k:
                left = next_left()
            else:
                right = next_right()
        return False
