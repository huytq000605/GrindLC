class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ds = [(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(maze), len(maze[0])
        def dfs(r, c):
            if r == destination[0] and c == destination[1]:
                return True
            for dr, dc in ds:
                nr, nc = r, c
                while 0 <= nr + dr < m and\
                        0 <= nc + dc < n and\
                        maze[nr + dr][nc + dc] != 1:
                    nr = nr + dr
                    nc = nc + dc
                if maze[nr][nc] == 0:
                    maze[nr][nc] = -1
                    if dfs(nr, nc):
                        return True
            return False
        return dfs(start[0], start[1])

                 
