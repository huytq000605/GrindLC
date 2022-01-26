# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left
        s1, s2 = [], []
        push_left(root1, s1)
        push_left(root2, s2)
        result = []
        while len(s1) > 0 or len(s2) > 0:
            if len(s1) == 0:
                while len(s2) > 0:
                    top = s2.pop()
                    result.append(top.val)
                    push_left(top.right, s2)
            elif len(s2) == 0:
                while len(s1) > 0:
                    top = s1.pop()
                    result.append(top.val)
                    push_left(top.right, s1)
            else:
                if s1[-1].val <= s2[-1].val:
                    top = s1.pop()
                    top_stack = s1
                else:
                    top = s2.pop()
                    top_stack = s2
                result.append(top.val)
                push_left(top.right, top_stack)
        return result
            