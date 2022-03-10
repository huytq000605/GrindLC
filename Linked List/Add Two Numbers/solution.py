# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
				
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1 = l1.val
            if l2: v2 = l2.val
            if not current.next:
                current.next = ListNode(0)
            current = current.next
            current.val += v1 + v2
            if current.val >= 10:
                current.val %= 10
                current.next = ListNode(1)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next