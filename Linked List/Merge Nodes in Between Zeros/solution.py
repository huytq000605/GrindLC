# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0, None)
        val = 0
        head = head.next
        while head:
            if head.val == 0:
                cur.next = ListNode(val, None)
                cur = cur.next
                val = 0
            else:
                val += head.val
            head = head.next
        return dummy.next
