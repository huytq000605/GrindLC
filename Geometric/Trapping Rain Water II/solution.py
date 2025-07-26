class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        visited = [[False for j in range(n)] for i in range(m)]
        
        heap = []
        for row in [0, m - 1]:
            for col in range(n):
                heappush(heap, [heightMap[row][col], row, col])
                visited[row][col] = True
        
        for col in [0, n - 1]:
            for row in range(m):
                if row == 0 or row == m - 1:
                    continue
                heappush(heap, [heightMap[row][col], row, col])
                visited[row][col] = True
            
        minHeight = -math.inf
        result = 0
        
        
        
        while len(heap):
            height, row, col = heappop(heap)
            minHeight = max(minHeight, height)
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]
                if nrow < 0 or nrow >= m or ncol < 0 or ncol >= n or visited[nrow][ncol] is True:
                    continue
                if heightMap[nrow][ncol] < minHeight:
                    result += minHeight - heightMap[nrow][ncol]
                heappush(heap, [max(minHeight, heightMap[nrow][ncol]), nrow, ncol])
                visited[nrow][ncol] = True
        return result
        
