# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = -1
        current = head
        while current:
            length += 1
            current = current.next
        result = 0
        current = head
        while current:
            result += current.val << length
            length -= 1
            current = current.next
        return result