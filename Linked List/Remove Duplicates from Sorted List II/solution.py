# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(node):
            if not node:
                return
            current = node.next
            get_this = True
            
            while current and current.val == node.val:
                get_this = False
                current = current.next
                
            if get_this:
                node.next = recursion(current)
                return node
            else:
                return recursion(current)
        return recursion(head)