from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            head = TreeNode(val, root)
            return head
        queue = deque([[root, 1]])
        while len(queue) > 0:
            current = queue.popleft()
            left = current[0].left
            right = current[0].right
            if current[1] == depth - 1:
                current[0].left = TreeNode(val, left)
                current[0].right = TreeNode(val, None, right)
            if current[1] > depth - 1:
                break
            if left != None:
                queue.append([left, current[1]+1])
            if right != None:
                queue.append([right, current[1]+1])
        return root