class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, dia1, dia2 = set(), set(), set()
        result = set()
        matrixs = []
        grid = [["." for j in range(n)] for i in range(n)]
        def dfs(row):
            nonlocal n, cols, dia1, dia2, matrixs
            if row >= n:
                matrixs.append(["".join(grid[i]) for i in range(n)])
            for col in range(n):
                if col in cols or row + col in dia1 or row - col in dia2:
                    continue
                cols.add(col)
                dia1.add(row + col)
                dia2.add(row - col)
                grid[row][col] = "Q"
                dfs(row + 1)
                cols.discard(col)
                dia1.discard(row+col)
                dia2.discard(row-col)
                grid[row][col] = "."
            return False
        dfs(0)
        return matrixs
