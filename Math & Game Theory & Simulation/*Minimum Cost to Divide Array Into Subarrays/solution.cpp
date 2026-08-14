class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        prefix = list(accumulate(nums, initial = 0))
        prefix_cost = list(accumulate(cost, initial = 0))
        n = len(nums)
        @cache
        def dfs(i):
            # K(∑p​p∗Cip​..jp​​) --> K(∑p​Cip​..​)
            # C1 + 2C2 + 3C3
            # = (C1 + C2 + C3) + (C2 + C3) + (C3)
            if i == n:
                return 0
            result = math.inf
            for j in range(i, n):
                c = prefix[j+1] * (prefix_cost[j+1] - prefix_cost[i])
                c += k * (prefix_cost[-1] - prefix_cost[i])
                c += dfs(j+1)
                result = min(result, c)
            return result
        
        return dfs(0)
