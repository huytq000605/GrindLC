# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        max_distance = -1
        min_distance = math.inf

        first = -1
        last = -1

        prev = head.val
        i = 0
        head = head.next
        while head and head.next:
            cur = head.val
            nxt = head.next.val
            if (cur < nxt and cur < prev) or (cur > nxt and cur > prev):
                if last != -1:
                    max_distance = i - first
                    min_distance = min(min_distance, i - last)
                if first == -1: first = i
                last = i
            prev = cur
            i += 1
            head = head.next
        if max_distance == -1: return [-1, -1]
        return [min_distance, max_distance]
