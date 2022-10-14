# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        dumb = ListNode(0, head)
        slow, fast = dumb, dumb
        while fast:
            if not fast.next or not fast.next.next:
                slow.next = slow.next.next
                return head
            slow = slow.next
            fast = fast.next.next
        return head
