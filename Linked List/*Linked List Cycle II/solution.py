# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if not cycle:
            return None
        # a = from head to start of cycle
        # b = from start of cycle to meet point
        # s1 = a + b
        # s2 = 2 * (a + b)
        # s2 - s1 = k * cycle
        # a + b = k * cycle
        # => if slow go more a, slow it will come to the start of cycle
        while slow != head:
            head = head.next
            slow = slow.next
        return head
        
