# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(-1)
        greater_or_equal = ListNode(-1)
        u, v = less, greater_or_equal
        while head:
            if head.val < x:
                u.next = head
                u = u.next
            else:
                v.next = head
                v = v.next
            head = head.next
        u.next = greater_or_equal.next
        v.next = None
        return less.next
