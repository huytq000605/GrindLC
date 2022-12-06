# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(0), ListNode(0)
        dummy_odd = odd
        dummy_even = even
        i = 1
        while head:
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            i += 1
        odd.next = dummy_even.next
        even.next = None
        return dummy_odd.next
