# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    # Reservoir Sampling
    def getRandom(self) -> int:
        cur = self.head
        n = 0
        result = 0
        while cur != None:
            n += 1
            if random.randint(0, n - 1) < 1:
                result = cur.val
            cur = cur.next
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
