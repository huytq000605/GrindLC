class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click
        def click(r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return False
            if board[r][c] == 'E':
                count = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == dc == 0: continue
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                        count += board[nr][nc] == 'M'
                board[r][c] = str(count) if count else 'B'
                if not count:
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if dr == dc == 0: continue
                            nr, nc = r + dr, c + dc
                            if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                            if not click(nr, nc): return False
                return True
            return True
        click(r, c)
        return board
