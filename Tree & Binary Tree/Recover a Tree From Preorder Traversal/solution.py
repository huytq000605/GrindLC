# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        level = 0
        val = 0
        root = None
        traversal += '-'
        for l in traversal:
            if l.isdigit():
                val = val * 10 + int(l)
            else:
                if val != 0:
                    node = TreeNode(val)
                    if not root:
                        root = node
                    while stack and stack[-1][1] + 1 > level:
                        stack.pop()

                    if stack and stack[-1][1] + 1 == level:
                        if not stack[-1][0].left:
                            stack[-1][0].left = node
                        else:
                            stack[-1][0].right = node
                    stack.append((node, level))
                    level = 0
                    val = 0
                level += 1
        return root
