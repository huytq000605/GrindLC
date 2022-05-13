"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        node = root
        while node:
            # This dummy to store next level node as next
            dummy = Node(0)
            
            # store pointer to node on the left
            pointer = dummy
            
            # process all child node of current level
            while node:
                if node.left:
                    pointer.next = node.left
                    pointer = pointer.next
                if node.right:
                    pointer.next = node.right
                    pointer = pointer.next
                node = node.next
            node = dummy.next
        return root