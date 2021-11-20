# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        def dfs(prevLevel):
            nonlocal i
            current = 0
            level = 0
            index = i
            
            while index < len(traversal) and traversal[index] == "-":
                level += 1
                index += 1
            
            if level != prevLevel + 1:
                return
            
            i = index
            while i < len(traversal) and traversal[i].isdigit():
                current = current * 10 + int(traversal[i])
                i += 1
                
            node = TreeNode(current)
            node.left = dfs(level)
            node.right= dfs(level)
            return node
        return dfs(-1)
            