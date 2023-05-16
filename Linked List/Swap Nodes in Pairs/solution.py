# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        a = head
        head = head.next
        while a and a.next:
            c = a.next.next
            b = a.next
            if prev:
                prev.next = b
            prev = a

            b.next = a
            a.next = c

            a = c
        return head
