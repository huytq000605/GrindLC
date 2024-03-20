# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail_list2 = list2
        while tail_list2.next:
            tail_list2 = tail_list2.next
        i = 0
        cur = list1
        for _ in range(a-1):
            cur = cur.next
        nxt = cur.next
        cur.next = list2
        cur = nxt
        for _ in range(b - a + 1):
            cur = cur.next
        tail_list2.next = cur
        return list1

        
