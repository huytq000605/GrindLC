class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0 for j in range(n)] for i in range(m)]
        result = 0
        
        def numSubArray(array):
            nonlocal target
            current = 0
            prefix = dict()
            prefix[0] = 1
            result = 0
            for i in range(len(array)):
                current += array[i]
                if current - target in prefix:
                    result += prefix[current - target]
                prefix[current] = prefix.get(current, 0) + 1
            return result
        
		# Calculate prefix sum for each column to quickly lookup sum of each column for a range of row
        for row in range(m):
            for col in range(n):
                if row > 0:
                    prefix[row][col] = prefix[row - 1][col]
                prefix[row][col] += matrix[row][col]
        
		# Create a range of row [startRow, endRow], sum of each column from startRow to endRow as an element of an array
		# => Find subarray sum to target
        for startRow in range(m):
            for endRow in range(startRow, m):
                arr = [0] * n
                for col in range(n):
                    if startRow > 0:
                        arr[col] = prefix[endRow][col] - prefix[startRow - 1][col]
                    else:
                        arr[col] = prefix[endRow][col]
                
                result += numSubArray(arr)
        
        return result
        
                    