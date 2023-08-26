class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i, prev):
            if i == n:
                return 0
            result = math.inf
            for j in range(prev, 4):
                res = dfs(i+1, j)
                if j != nums[i]:
                    res += 1
                result = min(res, result)
            return result
        return min([dfs(0, i) for i in range(1, 4)])
                
