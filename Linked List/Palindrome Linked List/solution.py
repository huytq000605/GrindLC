# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next

            nxt_slow = slow.next
            slow.next = prev
            prev = slow
            slow = nxt_slow

        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != prev.val: return False
            slow = slow.next
            prev = prev.next
        return True
