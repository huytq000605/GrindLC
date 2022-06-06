# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # len(A) = a + c
        # len(B) = b + c
        # if pointer1 and pointer2 both traverse a+c+b then they will meet
        # if there is no intersection, pointer1 and pointer2 will both traverse a+b+c+c and be null
        a, b = headA, headB
        while a != b:
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next
        return a
        