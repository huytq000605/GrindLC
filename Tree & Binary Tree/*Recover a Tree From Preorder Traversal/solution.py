# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            level = 0
            current = 0
            while traversal[i] == "-":
                level += 1
                i += 1
            
            while i < len(traversal) and traversal[i].isdigit():
                current = current * 10 + int(traversal[i])
                i += 1
                
                
            node = TreeNode(current)
            
            while len(stack) and level <= stack[-1][1]:
                stack.pop()
            if len(stack):
                if stack[-1][0].left == None:
                    stack[-1][0].left = node
                else:
                    stack[-1][0].right = node
            stack.append([node, level])
            
        return stack[0][0]