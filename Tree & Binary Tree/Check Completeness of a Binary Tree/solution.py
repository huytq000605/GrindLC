from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        flag = False
        while len(queue) > 0:
            current = queue.popleft()
            if flag == True and current != None:
                return False
            if current == None:
                flag = True
                continue
            queue.append(current.left)
            queue.append(current.right)
            
        return True
        