# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = ListNode(-math.inf)
        prevHead.next = head
        
        while head and head.next:
            while head.next and head.next.val < head.val:
                swapNode = head.next
                head.next = head.next.next
            
                current = prevHead
                while current.next.val < swapNode.val:
                    current = current.next
                
                originalNext = current.next
                current.next = swapNode
                swapNode.next = originalNext
                
            head = head.next
        return prevHead.next