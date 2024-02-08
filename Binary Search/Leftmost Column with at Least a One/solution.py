# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, matrix: 'BinaryMatrix') -> int:
        m, n = matrix.dimensions()
        result = n+1
        for r in range(m):
            start = 0
            end = n
            while start < end:
                mid = start + (end - start) // 2
                if matrix.get(r, mid) == 0:
                    start = mid + 1
                else:
                    end = mid
            if start < n: result = min(result, start)
        if result == n+1: return -1
        return result
