
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for j in range(n)] for i in range(m)]
        min_row = min_col = 0
        max_row = m - 1
        max_col = n - 1

        while min_row <= max_row and min_col <= max_col:
            if not head:
                break
            for c in range(min_col, max_col + 1):
                result[min_row][c] = head.val
                head = head.next
                if not head:
                    break

            if not head:
                break
            for r in range(min_row + 1, max_row + 1):
                result[r][max_col] = head.val
                head = head.next
                if not head:
                    break

            if not head:
                break
            for c in range(max_col - 1, min_col - 1, -1):
                result[max_row][c] = head.val
                head = head.next
                if not head:
                    break

            if not head:
                break
            for r in range(max_row - 1, min_row, -1):
                result[r][min_col] = head.val
                head = head.next
                if not head:
                    break

            max_row -= 1
            max_col -= 1
            min_row += 1
            min_col += 1
        return result
