"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node

        prev = head
        cur = head.next
        while True:
            if prev.val <= insertVal <= cur.val \
                or (prev.val > cur.val and insertVal > prev.val) \
                or (prev.val > cur.val and insertVal < cur.val):
                prev.next = Node(insertVal, cur)
                return head
            
            prev = cur
            cur = cur.next
            if prev == head: break
        head.next = Node(insertVal, head.next)
        return head
