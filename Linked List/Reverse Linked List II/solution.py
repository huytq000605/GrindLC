# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        prev, cur = None, head
        i = 1
        while i < left:
            prev = cur
            cur = cur.next
            i += 1
        
        prev_reverse = prev
        start_reverse = cur
        while i <= right:
            nxt = cur.next
            cur.next = prev
            
            prev = cur
            cur = nxt
            i += 1
        
        if prev_reverse:
            prev_reverse.next = prev
        start_reverse.next = cur
        
        if left == 1:
            return prev
        return head
                    
                    
                
