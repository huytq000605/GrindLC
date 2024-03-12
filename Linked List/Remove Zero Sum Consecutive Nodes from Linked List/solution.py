# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefixs = dict()
        prefix = 0
        ptr = dummy
        while ptr:
            prefix += ptr.val
            if prefix in prefixs:
                ptr = prefixs[prefix].next
                p = prefix + ptr.val
                while p != prefix:
                    prefixs.pop(p)
                    ptr = ptr.next
                    p += ptr.val
                prefixs[prefix].next = ptr.next
            else:
                prefixs[prefix] = ptr
            ptr = ptr.next
        return dummy.next
                
