class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [[[0, 0] for j in range(n)] for i in range(m)]
        result = 0
        
        @cache
        def two_five_factors(num):
            two, five = 0, 0
            while num % 2 == 0 and num > 0:
                num //= 2
                two += 1
            
            while num % 5 == 0 and num > 0:
                num //= 5
                five += 1
            return two, five
        
        for row in range(m):
            for col in range(n):
                if col > 0:
                    rows[row][col][0] = rows[row][col-1][0]
                    rows[row][col][1] = rows[row][col-1][1]
                factors = two_five_factors(grid[row][col])
                for j in range(2):
                    rows[row][col][j] += factors[j]
                    
				# Each column
        for col in range(n):
            current = [0, 0]
						# Go from top to bottom
            for row in range(m):
                if col == 0:
                    result = max(result, min(rows[row][n - 1][0] + current[0], rows[row][n - 1][1] + current[1]))
                else:
                    result = max(
                        result, 
                        min(rows[row][n-1][0] - rows[row][col - 1][0] + current[0], rows[row][n-1][1] - rows[row][col - 1][1] + current[1]),
                        min(rows[row][col][0] + current[0], rows[row][col][1] + current[1])           
                    )
                factors = two_five_factors(grid[row][col])
                current[0] += factors[0]
                current[1] += factors[1]
    
            current = [0, 0]
						# Go from bottom to top
            for row in range(m - 1, -1 ,-1):
                if col == 0:
                    result = max(result, min(rows[row][n - 1][0] + current[0], rows[row][n - 1][1] + current[1]))
                else:
                    result = max(
                        result, 
                        min(rows[row][n-1][0] - rows[row][col - 1][0] + current[0], rows[row][n-1][1] - rows[row][col - 1][1] + current[1]),
                        min(rows[row][col][0] + current[0], rows[row][col][1] + current[1])           
                    )
                factors = two_five_factors(grid[row][col])
                current[0] += factors[0]
                current[1] += factors[1]
        return result
                    