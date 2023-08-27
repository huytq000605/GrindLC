# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        while head:
            nxt = head.next
            if not nxt:
                break
            new_node = ListNode(math.gcd(head.val, nxt.val))
            head.next = new_node
            new_node.next = nxt
            head = nxt
        return result
