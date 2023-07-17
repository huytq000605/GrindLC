# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev_ll(u):
            prev = None
            while u:
                v = u.next
                u.next = prev
                prev = u
                u = v
            return prev
        l1, l2 = rev_ll(l1), rev_ll(l2)
        r = 0
        result = ListNode(0)
        cur = result
        while l1 or l2:
            value = r
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            cur.next = ListNode(value % 10)
            cur = cur.next
            r = value // 10
        if r: cur.next = ListNode(r)
        return rev_ll(result.next)

