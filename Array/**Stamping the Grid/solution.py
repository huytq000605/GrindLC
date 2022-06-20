class Solution:
    def possibleToStamp(self, grid: List[List[int]], H: int, W: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        def prefix_grid(grid):
            prefix = [[0 for j in range(n + 1)] for i in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + grid[i][j]
            return prefix
        
        def sum_region(prefix, r1, c1, r2, c2):
            return prefix[r2+1][c2+1] - prefix[r2+1][c1] - prefix[r1][c2+1] + prefix[r1][c1]
        
        prefix_sum_grid = prefix_grid(grid)
        
        # Because we need start and end so diff has size+1
        diff = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m - H + 1):
            for j in range(n - W + 1):
								# If we can put a stamp start here
                if sum_region(prefix_sum_grid, i, j, i + H -1, j + W -1) == 0:
									# Remember sweepline problems, when we have a row, we wanna see do position from 1 to 4 have passengers?
									# We do something like arr[1] += 1, arr[4] -= 1 and see their prefix sum
                    diff[i][j] += 1
                    diff[i+H][j] -= 1
                    diff[i][j+W] -= 1
                    diff[i+H][j+W] += 1
        
				# Calculate prefix sum to lookup quickly a position have stamp or not? (have stamp => != 0)
        prefix_sum_diff = prefix_grid(diff)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and prefix_sum_diff[i+1][j+1] == 0:
                    return False
        
        return True