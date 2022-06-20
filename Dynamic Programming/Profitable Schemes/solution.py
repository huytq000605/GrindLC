class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i, current_people, current_profit):
            if i >= len(group):
                if current_profit >= minProfit:
                    return 1
                return 0
            result = 0
            if current_people >= group[i]:
                result += dfs(i + 1, current_people - group[i], min(minProfit, current_profit + profit[i]))
            result += dfs(i + 1, current_people, current_profit)
            return result % (10**9 + 7)
        return dfs(0, n, 0)