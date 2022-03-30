class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m - 1
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid
                
        row = start
        if matrix[row][0] > target:
            return False
        
        start = 0
        end = n - 1
        while start < end:
            mid = start + (end - start) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid
        return matrix[row][start] == target