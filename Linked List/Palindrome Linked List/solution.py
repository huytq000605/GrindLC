# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, slow, fast = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            cur_slow, slow = slow, slow.next
            cur_slow.next, prev = prev, cur_slow
        if fast:
            slow = slow.next
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
