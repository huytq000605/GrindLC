class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache(None)
        def dfs(i):
            if i == n:
                return 0
            cost = math.inf
            counter = defaultdict(int)
            s = 0
            for j in range(i, n):
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    s += 2
                elif counter[nums[j]] > 2:
                    s += 1
                cost = min(cost, k + s + dfs(j + 1))
            return cost
        return dfs(0)
