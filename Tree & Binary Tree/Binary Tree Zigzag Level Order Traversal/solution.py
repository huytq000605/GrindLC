from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([[root, 0]])
        previousLevel = 0
        goLeftToRight = True
        result = [deque([])]
        while len(queue) > 0:
            [currentNode, currentLevel] = queue.popleft()
            if currentLevel != previousLevel:
                result.append(deque([]))
                goLeftToRight = not goLeftToRight
            if goLeftToRight:
                result[currentLevel].append(currentNode.val)
            else:
                result[currentLevel].appendleft(currentNode.val)
            previousLevel = currentLevel
            if currentNode.left:
                queue.append([currentNode.left, currentLevel + 1])
            if currentNode.right:
                queue.append([currentNode.right, currentLevel + 1])
        return result
        