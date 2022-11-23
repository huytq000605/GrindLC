class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs():
            for r in range(m):
                for c in range(n):
                    if board[r][c] == ".":
                        for v in range(1, 10):
                            v = str(v)
                            if is_valid(r, c, v):
                                board[r][c] = v
                                if dfs(): return True
                                board[r][c] = "."
                        return False
            return True
            
            
        def is_valid(r, c, v):
            for i in range(9):
                if board[i][c] == v: return False
                if board[r][i] == v: return False
                if board[r // 3 * 3 + i // 3][c // 3 * 3 + i % 3] == v: return False
            return True
        
        dfs()
        
