# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        else:
            return head
        
        first = self.sortList(head)
        second = self.sortList(slow)
        return self.merge(first, second)
    
    def merge(self, first, second):
        if not second:
            return first
        if first.val <= second.val:
            head = first
            first = first.next
        else:
            head = second
            second = second.next
        current = head
        while first and second:
            if first.val <= second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next
        
        remaining = first or second
        while remaining:
            current.next = remaining
            remaining = remaining.next
            current = current.next
        return head
                