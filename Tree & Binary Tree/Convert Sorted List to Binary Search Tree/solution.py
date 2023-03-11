# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
            
        cur = head
        def dfs(start, end):
            nonlocal cur
            if start > end:
                return None
            mid = start + (end - start) // 2
            left = dfs(start, mid - 1)
            node = TreeNode(cur.val)
            cur = cur.next
            right = dfs(mid + 1, end)
            node.left = left
            node.right = right
            return node
        return dfs(0, n-1)
