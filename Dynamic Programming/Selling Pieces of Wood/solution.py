class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        price = [[0 for j in range(n+1)] for i in range(m+1)]
        for h, w, p in prices:
            price[h][w] = p
        @cache
        def dfs(rows, cols):
            if cols == 0 or rows == 0:
                return 0
            result = price[rows][cols]
            for i in range(1, rows // 2 + 1):
                result = max(result, dfs(i, cols) + dfs(rows - i, cols))
            for i in range(1, cols // 2 + 1):
                result = max(result, dfs(rows, i) + dfs(rows, cols - i))
            return result
        return dfs(m, n)