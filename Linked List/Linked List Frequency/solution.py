# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)
        while head:
            freq[head.val] += 1
            head = head.next
        dummy = ListNode(0, None)
        cur = dummy
        for val in freq.values():
            cur.next = ListNode(val, None)
            cur = cur.next
        return dummy.next
