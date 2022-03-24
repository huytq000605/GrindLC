class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        dp_score = [[0 for j in range(n)] for i in range(m)]
        dp_paths = [[0 for j in range(n)] for i in range(m)]
        dp_paths[m-1][n-1] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if dp_paths[r][c] == 0:
                    continue
                for d in [(-1, -1), (-1, 0), (0, -1)]:
                    nr, nc = r + d[0], c + d[1]
                    if board[nr][nc] == "X" or nr < 0 or nc < 0:
                        continue
                    if board[nr][nc] == "E":
                        value = 0
                    else:
                        value = int(board[nr][nc])
                    if dp_score[nr][nc] < dp_score[r][c] + value:
                        dp_score[nr][nc] = dp_score[r][c] + value
                        dp_paths[nr][nc] = dp_paths[r][c]
                    elif dp_score[nr][nc] == dp_score[r][c] + value:
                        dp_paths[nr][nc] += dp_paths[r][c]
                        dp_paths[nr][nc] %= (10**9 + 7)
        return [dp_score[0][0], dp_paths[0][0]]