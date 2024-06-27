# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefixes = dict()
        prefix = 0
        ptr = dummy
        while ptr:
            prefix += ptr.val
            if prefix in prefixes:
                start_remove = prefixes[prefix].next
                cur = prefix + start_remove.val
                while start_remove != ptr:
                    prefixes.pop(cur, None)
                    start_remove = start_remove.next
                    cur += start_remove.val
                prefixes[prefix].next = ptr.next
            else:
                prefixes[prefix] = ptr
            ptr = ptr.next
        return dummy.next
            
                
