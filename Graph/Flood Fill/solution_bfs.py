class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = deque([[sr, sc]])
        m = len(image)
        n = len(image[0])
        dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
        color = image[sr][sc]
        if color == newColor:
            return image
        while queue:
            r, c = queue.popleft()
            image[r][c] = newColor
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or image[nr][nc] != color:
                    continue
                queue.append([nr, nc])
        return image