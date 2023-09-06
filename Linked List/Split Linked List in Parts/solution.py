# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        each = n // k
        remaining = n % k
        result = [None for _ in range(k)]
        
        for i in range(k):
            if not head:
                break
            result[i] = head
            m = each - 1
            if remaining:
                m += 1
                remaining -= 1
            for _ in range(m):
                head = head.next
            if not head:
                break
            nxt = head.next
            head.next = None
            head = nxt
                
        return result
            
