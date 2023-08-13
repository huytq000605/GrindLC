# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
            num = num * 10 + cur.val
            cur = cur.next
        if num == 0:
            return ListNode(0)
        num *= 2
        
        s = []
        while num:
            s.append(num % 10)
            num //= 10
        
        result = ListNode(0)
        cur = result
        while s:
            d = s.pop()
            cur.next = ListNode(d)
            cur = cur.next
        return result.next
