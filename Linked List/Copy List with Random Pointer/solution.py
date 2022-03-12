# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = dict()
        current = head
        def get_copy(node):
            if not node:
                return None
            if node not in mapping:
                mapping[node] = Node(node.val)
            return mapping[node]
        
        while current:
            new_current = get_copy(current)
            new_current.next = get_copy(current.next)
            new_current.random = get_copy(current.random)
            current = current.next
        return get_copy(head)