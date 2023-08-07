class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        start = 0
        end = m*n-1
        
        while start < end:
            mid = start + (end - start) // 2
            if matrix[mid//n][mid%n] < target:
                start = mid + 1
            else:
                end = mid
        return matrix[start//n][start%n] == target
