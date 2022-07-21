# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur = None, head
        position = 1
        while cur:
            if position == left:
                prev_reverse = prev
                start_reverse = cur
                prev = None
                while cur and position != right + 1:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                    position += 1
                start_reverse.next = cur
                if prev_reverse:
                    prev_reverse.next = prev
                break
            prev = cur
            cur = cur.next
            position += 1
        if left == 1:
            return prev
        else:
            return head
