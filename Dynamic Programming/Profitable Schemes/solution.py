class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        MOD = 10**9 + 7
        @cache
        def dfs(i, people, prof):
            if i >= m:
                if prof >= minProfit: return 1
                return 0
            result = dfs(i + 1, people, prof)
            if people >= group[i]:
                result += dfs(i + 1, people - group[i], min(minProfit, prof + profit[i]))
            return result % MOD
        return dfs(0, n, 0)
