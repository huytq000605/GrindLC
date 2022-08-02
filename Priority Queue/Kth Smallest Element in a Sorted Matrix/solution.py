class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for i in range(n):
            heappush(min_heap, (matrix[i][0], i, 0))
        result = 0
        while k:
            val, row, col = heappop(min_heap)
            if col + 1 < n:
                heappush(min_heap, (matrix[row][col+1], row, col+1))
            result = val
            k -= 1
        return result
