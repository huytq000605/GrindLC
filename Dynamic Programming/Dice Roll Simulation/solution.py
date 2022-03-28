class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @cache
        def dfs(i, j, last_dice):
            if i >= n:
                return 1
            result = 0
            for dice in range(6):
                if dice == last_dice and i - j + 1 > rollMax[dice]:
                    continue
                if dice == last_dice:
                    result += dfs(i + 1, j, last_dice)
                else:
                    result += dfs(i + 1, i, dice)
            return result % (10**9 + 7)
        return dfs(0, -1, -1)