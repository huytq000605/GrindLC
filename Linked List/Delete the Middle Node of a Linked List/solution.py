# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        x = length // 2
        current = head
        index = 0
        if x == 0:
            return None
        while current:
            if index + 1 == x:
                current.next = current.next.next
                return head
            else:
                current = current.next
            index += 1