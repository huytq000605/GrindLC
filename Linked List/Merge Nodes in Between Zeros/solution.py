# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        current_node = result
        current = 0
        
        while head:
            if head.val == 0:
                current_node.next = ListNode(current)
                current_node = current_node.next
                current = 0
            else:
                current += head.val
            head = head.next
        return result.next.next