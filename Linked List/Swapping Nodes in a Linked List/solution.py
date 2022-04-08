# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
				
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        idx = 1
        a,b = head, head
        
        current = head
        while current:
            b = b.next
            if idx == k:
                a = current
                b = head
            current = current.next
            idx += 1
        a.val, b.val = b.val, a.val
        return head