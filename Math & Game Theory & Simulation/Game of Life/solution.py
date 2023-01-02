class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs =[(0,1), (1,0), (-1,0), (0, -1), (1,1), (1,-1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                lives = 0
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    if board[nr][nc] >= 1:
                        lives += 1
                if board[r][c] >= 1:
                    if lives < 2 or lives > 3:
                        board[r][c] = 2
                else:
                    if lives == 3:
                        board[r][c] = -1
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == -1:
                    board[r][c] = 1