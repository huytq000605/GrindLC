class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        @cache
        def dfs(idx, carpets):
            if carpets < 0:
                return math.inf
            if idx >= n:
                return 0
            plus = 0
            if floor[idx] == '1':
                plus = 1
            return min(dfs(idx + carpetLen, carpets - 1), dfs(idx + 1, carpets) + plus)
        return dfs(0, numCarpets)