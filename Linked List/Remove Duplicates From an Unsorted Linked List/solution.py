# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = Counter()

        cur = head
        while cur:
            counter[cur.val] += 1
            cur = cur.next
        
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if counter[head.val] > 1:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dummy.next
            
                
