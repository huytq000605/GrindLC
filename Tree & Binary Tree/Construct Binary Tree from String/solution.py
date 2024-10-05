# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None
        val = 0
        i = 0
        negative = False
        while i < len(s):
            if s[i] == "-": 
                negative = True
                i += 1
                continue
            
            if not s[i].isdigit(): break
            val = val * 10 + int(s[i])
            i += 1
        if negative: val = -val

        left = ""
        if i < len(s) and s[i] == "(":
            start = i
            stack = 0
            while i < len(s):
                if s[i] == "(":
                    stack += 1
                if s[i] == ")":
                    stack -= 1
                i += 1
                if not stack: break
            left = s[start+1:i]
        
        right = ""
        if left and i < len(s) and s[i] == "(":
            start = i
            stack = 0
            while i < len(s):
                if s[i] == "(":
                    stack += 1
                if s[i] == ")":
                    stack -= 1
                i += 1
                if not stack: break
            right = s[start+1:i]
        
        return TreeNode(val, self.str2tree(left), self.str2tree(right))

