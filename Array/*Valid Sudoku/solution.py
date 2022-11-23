class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for r in range(m):
            for c in range(n):
                v = board[r][c]
                if v != ".":
                    if v in rows[r]: return False
                    if v in cols[c]: return False
                    square_idx = r // 3 * 3 + c // 3
                    if v in squares[square_idx]: return False
                    rows[r].add(v)
                    cols[c].add(v)
                    squares[square_idx].add(v)
        return True
