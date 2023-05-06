class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        MOD = 10**9 + 7
        j = n-1

        @cache
        def pow2_cache(n):
            if n == 0: return 1
            return (pow2_cache(n-1) * 2) % MOD
        
        for i in range(n):
            while j >= i and nums[j] + nums[i] > target:
                j -= 1
            if j >= i and nums[j] + nums[i] <= target:
                result += pow2_cache(j-i)
                result %= MOD
        return result
