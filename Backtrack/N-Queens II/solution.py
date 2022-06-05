class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, dia1, dia2 = set(), set(), set()
        def dfs(row):
            if row >= n:
                return 1
            result = 0
            for col in range(n):
                if col in cols or row + col in dia1 or row - col in dia2:
                    continue
                cols.add(col)
                dia1.add(row + col)
                dia2.add(row - col)
                result += dfs(row + 1)
                cols.discard(col)
                dia1.discard(row + col)
                dia2.discard(row - col)
            return result
        return dfs(0)