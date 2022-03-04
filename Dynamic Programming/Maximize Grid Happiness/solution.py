class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @cache
        def dfs(row, col, prev_row, prev_col, i, e):
            # m * n * 2^(2*n) * 3 * m * n
            if col >= n:
                return dfs(row + 1, 0, prev_row, 0, i, e)
            if row >= m:
                return 0
            result = 0
            for value in range(3):
                if value == 1 and i == 0:
                    continue
                if value == 2 and e == 0:
                    continue
                next_i, next_e = i, e
                ans = 0
                top_cell = (prev_row >> (2*col)) & 3
                if value == 0:
                    new_row = prev_row & ~(3 << (2*col))
                elif value == 1:
                    ans = 120
                    next_i -= 1
                    if prev_col == 1:
                        ans -= 2 * 30
                    elif prev_col == 2:
                        ans = ans + 20 - 30
                    
                    if top_cell == 1:
                        ans -= 2 * 30
                    elif top_cell == 2:
                        ans = ans + 20 - 30
                    new_row = prev_row & ~(3 << (2*col))
                    new_row |= (1 << (2*col))
                else:
                    ans = 40
                    next_e -= 1
                    if prev_col == 1:
                        ans = ans + 20 - 30
                    elif prev_col == 2:
                        ans += 20 * 2
                        
                    if top_cell == 1:
                        ans = ans + 20 - 30
                    elif top_cell == 2:
                        ans += 20 * 2
                    new_row = prev_row & ~(3 << (2*col))
                    new_row |= (2 << (2*col))
                result = max(result, ans + dfs(row, col + 1, new_row, value, next_i, next_e))
            return result
        return dfs(0, 0, 0, 0, introvertsCount, extrovertsCount)
            