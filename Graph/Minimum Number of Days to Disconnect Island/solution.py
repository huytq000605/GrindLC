class Solution:
	# There are only 3 possbile answers
	# If the grid has != 1 island => Return 0
	# If we can change 1 land to water to have != 1 island => Return 1
	# Else we just 2 days to make disconnected island
	# Example, disconnect the right of topleft and the bottom of topleft
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        
        def count_island(removed_row, removed_col):
            islands = 0
            seen = set()
            def dfs(i, j):
                for d in dirs:
                    nr, nc = i + d[0], j + d[1]
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in seen or (nr, nc) == (removed_row, removed_col) or grid[nr][nc] == 0:
                        continue
                    seen.add((nr, nc))
                    dfs(nr, nc)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) != (removed_row, removed_col):
                        if (i, j) not in seen:
                            seen.add((i,j))
                            islands += 1
                            dfs(i, j)
                        
            return islands

		# Remove (-1, -1) => day 0
        if count_island(-1, -1) != 1:
            return 0
		# Try to remove 1
        for i in range(m):
            for j in range(n):
                if count_island(i, j) != 1:
                    return 1
		# Just return 2
        return 2
            
        
