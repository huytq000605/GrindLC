class Solution:
    def numOfWays(self, n: int) -> int:
        colors = [1,2,3]
        dp = [[None for j in range(1 << 6)] for i in range(n)]
        MOD = 1e9 + 7
        
        def dfs(row, col, prevMask, currentMask):
            if row >= n:
                return 1
            if col >= 3:
                return dfs(row + 1, 0, currentMask, 0)
            if dp[row][prevMask] != None and col == 0:
                return dp[row][prevMask]
            top = (prevMask >> (2 * col)) & 0b11
            if col > 0:
                left = (currentMask >> (2 * (col - 1))) & 0b11
            else:
                left = 0
            result = 0
            for color in colors:
                if color == top or color == left:
                    continue
                newMask = currentMask | (color << (2*col))
                result += dfs(row, col + 1, prevMask, newMask)
                result = int(result % MOD)
            if col == 0:
                dp[row][prevMask] = result
            return result
        
        return dfs(0, 0, 0, 0)