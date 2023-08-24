class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        def crush():
            to_remove = []
            for r in range(m):
                c = 0
                while c < n - 2:
                    if board[r][c] == board[r][c+1] == board[r][c+2] != 0:
                        val = board[r][c]
                        while c < n and board[r][c] == val:
                            to_remove.append((r, c))
                            c += 1
                    else:
                        c += 1
            
            for c in range(n):
                r = 0
                while r < m - 2:
                    if board[r][c] == board[r+1][c] == board[r+2][c] != 0:
                        val = board[r][c]
                        while r < m and board[r][c] == val:
                            to_remove.append((r, c))
                            r += 1
                    else:
                        r += 1
            
            for r, c in to_remove:
                board[r][c] = 0
            
            return len(to_remove) != 0
            
        def fall():
            for c in range(n):
                for r in reversed(range(m-1)):
                    if board[r][c] == 0:
                        continue
                    while r + 1 < m and board[r+1][c] == 0:
                        board[r+1][c], board[r][c] = board[r][c], board[r+1][c]
                        r += 1
        
        while crush():
            fall()
        return board
