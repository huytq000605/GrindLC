class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        dirs = [[0,1], [1,0], [0, -1], [-1,0]]
        m = len(grid)
        n = len(grid[0])
        catX = -1
        catY = -1
        mouseX = -1
        mouseY = -1
        foodX = -1
        foodY = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    catX = i
                    catY = j
                elif grid[i][j] == 'M':
                    mouseX = i
                    mouseY = j
                elif grid[i][j] == 'F':
                    foodX = i
                    foodY = j
        @cache
        def dfs(catX, catY, mouseX, mouseY, turn):
            if catX == mouseX and catY == mouseY:
                return False
            if catX == foodX and catY == foodY:
                return False
            if mouseX == foodX and mouseY == foodY:
                return True
			# Tricky part: Mouse will try to get to the food ASAP and dont wanna go back
			# So upperbound turns is m*n*2 (cat also moves)
            if turn > m*n*2:
                return False
            if turn % 2 == 1:
                for d in dirs:
                    for jump in range(catJump + 1):
                        ncatx = catX + d[0] * jump
                        ncaty = catY + d[1] * jump
                        if ncatx < 0 or ncatx >= m or ncaty < 0 or ncaty >= n or grid[ncatx][ncaty] == "#":
                            break
                        if not dfs(ncatx, ncaty, mouseX, mouseY, turn + 1): return False
                return True
            else:
                for d in dirs:
                    for jump in range(mouseJump + 1):
                        nmx = mouseX + d[0] * jump
                        nmy = mouseY + d[1] * jump
                        if nmx < 0 or nmx >= m or nmy < 0 or nmy >= n or grid[nmx][nmy] == "#":
                            break
                        if dfs(catX, catY, nmx, nmy, turn + 1): return True
                return False
        
        return dfs(catX, catY, mouseX, mouseY, 0)
            