# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        result = None
        while head:
            next_node = head.next
            if not next_node:
                break
            if not result:
                result = next_node
            next_loop = next_node.next
            if prev:
                prev.next = next_node
            next_node.next = head
            prev = head
            head.next = next_loop
            head = head.next
            
        if not result:
            return head
        return result