class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        total = 0
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        ones = set()
        
        def getIdx(row, col):
            return row * n + col
        
        def countOne(i, j, ones, seen):
            result = 1
            for d in dirs:
                nr, nc = i + d[0], j + d[1]
                idx = getIdx(nr, nc)
                if nr < 0 or nr >= m or nc < 0 or nc >= n or idx not in ones or idx in seen:
                    continue
                seen.add(getIdx(nr, nc))
                result += countOne(nr, nc, ones, seen)
            return result
    
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    ones.add(getIdx(i, j))
        
        dp = set()

        queue = deque([[ones, 0]])
        while queue:
            current, steps = queue.popleft()
            if len(current) == 0:
                return steps
            idx = next(iter(current))
            row = idx // n
            col = idx - row * n
            if countOne(row, col, current, set([idx])) != total - steps:
                return steps
            for value in set(current):
                current.remove(value)
                key = str(sorted(list(current)))
                if key not in dp:
                    queue.append([set(current), steps + 1])
                    dp.add(key)
                    
                current.add(value)
        
        return 1