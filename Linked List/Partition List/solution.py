# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = ListNode(0)
        gte = ListNode(0)
        u, v = lt, gte
        while head:
            if head.val < x:
                u.next = head
                u = u.next
            else:
                v.next = head
                v = v.next
            head = head.next
        u.next = gte.next
        v.next = None
        return lt.next

