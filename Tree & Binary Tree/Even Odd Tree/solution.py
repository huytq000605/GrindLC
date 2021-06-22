from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        previousLevel = 0
        previousValue = 0
        queue = deque([[root, 0]])
        while len(queue) > 0:
            [currentNode, currentLevel] = queue.popleft()
            if currentLevel != previousLevel:
                previousLevel = currentLevel
                previousValue = 0
            
            if currentLevel % 2 == 0:
                isEvenLevel = True
            else: isEvenLevel = False
                
            if isEvenLevel:
                if currentNode.val % 2 == 0:
                    return False
                if previousValue != 0 and currentNode.val <= previousValue:
                    return False
            else:
                if currentNode.val % 2 == 1:
                    return False
                if previousValue != 0 and currentNode.val >= previousValue:
                    return False
            
            if currentNode.left != None: queue.append([currentNode.left, currentLevel + 1])
            if currentNode.right != None: queue.append([currentNode.right, currentLevel + 1])
            previousValue = currentNode.val
        return True