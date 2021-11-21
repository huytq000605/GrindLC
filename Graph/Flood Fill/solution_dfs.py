class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
        color = image[sr][sc]
        def dfs(r, c):
            if image[r][c] == newColor:
                return
            image[r][c] = newColor
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or image[nr][nc] != color:
                    continue
                dfs(nr, nc)
        dfs(sr, sc)
        return image