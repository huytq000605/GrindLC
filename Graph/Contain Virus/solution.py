class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(r, c, visited, infected):
            perimeter = 0
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n or (nr, nc) in visited:
                    continue
                if grid[nr][nc] == 0:
                    perimeter += 1
                    infected.add((nr, nc))
                elif grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    perimeter += dfs(nr, nc, visited, infected)
            return perimeter
        
        def block(r, c):
            grid[r][c] = 2
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if grid[nr][nc] == 1:
                    block(nr, nc)
        
        def infect(r, c):
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    
            
        while True:
            areas = []
            visited = set()
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        visited.add((r, c))
                        will_be_infected = set()
                        perimeter = dfs(r, c, visited, will_be_infected)
                        areas.append((len(will_be_infected), r, c, perimeter))
            if not areas:
                break
            areas.sort()
            will_be_infected, r, c, perimeter = areas.pop()
            block(r, c)
            for r, c in visited:
                if grid[r][c] == 1:
                    infect(r, c)
            result += perimeter
        return result