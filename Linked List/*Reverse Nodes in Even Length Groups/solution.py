# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        curr = head
        groupLength = 1
        remain = 1
        
        prev = None
        
        while curr:
            
            if remain == groupLength and length < groupLength:
                groupLength = length
                remain = length
                
            if groupLength % 2 == 0 and remain == groupLength:
                newHead, newTail = self.reverse(curr, None, groupLength)
                prev.next = newHead
                curr.next = newTail
                prev = curr
                length -= groupLength
                groupLength += 1
                remain = groupLength
                curr = curr.next

                continue
            prev = curr
            curr = curr.next
            remain -= 1
            if remain == 0:
                groupLength += 1
                remain = groupLength
            length -= 1
            
        return head
                
        
        
    def reverse(self, head, prev, length):
        nextLoop = head.next
        head.next = prev
        if nextLoop == None:
            return head, None
        if length > 1:
            return self.reverse(nextLoop, head, length - 1)
        return head, nextLoop
        
        