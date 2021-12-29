# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque([root])
        while queue:
            next_level = deque()
            while queue:
                current = queue.popleft()
                if current.left:
                    next_level.append(current.left)
                if current.right:
                    next_level.append(current.right)
                if len(queue):
                    current.next = queue[0]
            queue = next_level
        
        return root
