# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        heap = []
        for node in lists:
            if node:
                heappush(heap, node)
        dummy = ListNode()
        current = dummy
        while heap:
            node = heappop(heap)
            if node.next:
                heappush(heap, node.next)
            current.next = node
            current = current.next
            current.next = None   
        return dummy.next
        
