# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        diff = 0
        while head:
            even = head.val
            odd = head.next.val
            if even > odd: diff += 1
            if odd > even: diff -= 1
            head = head.next.next
        if diff > 0: return "Even"
        elif diff < 0: return "Odd"
        return "Tie"
