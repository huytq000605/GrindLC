class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < k*2:
            return 0
        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def dfs(i, s):
            if i >= n:
                return 1
            ignore = dfs(i+1, s)
            if s + nums[i] >= k:
                return ignore
            return ignore + dfs(i+1, s + nums[i])
        result = (2**n) - 2*dfs(0,0)
        return result % MOD
            
            
            
