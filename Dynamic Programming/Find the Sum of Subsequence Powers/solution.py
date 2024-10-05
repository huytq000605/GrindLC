class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        result = 0
        n = len(nums)
        nums.sort()
        @cache
        def dfs(diff, i, k, eq_diff, matched):
            if k == 0 and matched:
                return 1
            if i >= len(nums) or k < 0:
                return 0
            result = dfs(diff, i + 1, k, eq_diff and i+1<n and nums[i+1]==nums[i], matched)
            next_idx = bisect.bisect_left(nums, nums[i] + diff)
            result += dfs(diff, next_idx, k - 1, next_idx<n and nums[next_idx]==nums[i]+diff, matched or eq_diff)
            result %= MOD
            return result
        
        diffs = set()
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]
                if diff in diffs: continue
                diffs.add(diff)
                subsequences = dfs(diff, 0, k, 0, 0)
                result = (result + diff * subsequences) % MOD
        return result
