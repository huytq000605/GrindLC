# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        oddHead = head
        evenHead = head.next
        if not evenHead:
            return head
        odd = head
        even = head.next
        
        i = 1
        while head:
            if i <= 2:
                head = head.next
                i += 1
                continue
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            i += 1
            head = head.next
        
        odd.next = evenHead
        even.next = None
        return oddHead