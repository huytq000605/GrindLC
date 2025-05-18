class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def get_cols(prev_col):
            result = []
            get_cols_with_row(prev_col, 0, 0, result)
            return result

        def get_cols_with_row(prev_col, current_row, row, result):
            if row == m:
                result.append(current_row)
                return
            for color in range(1, 4):
                if row and color == (current_row >> (2*(row-1))) & 0b11: continue
                if prev_col != -1 and color == (prev_col >> (2*row)) & 0b11: continue
                get_cols_with_row(prev_col, current_row | (color << (2*row)), row + 1, result)

        @cache
        def dfs(col, prev_col):
            if(col >= n): return 1
            result = 0
            for b in get_cols(prev_col):
                result = (result + dfs(col + 1, b)) % MOD

            return result
        
        result = dfs(0, -1)
        dfs.cache_clear()
        return result
