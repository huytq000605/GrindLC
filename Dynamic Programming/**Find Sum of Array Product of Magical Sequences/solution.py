class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # looping from value of seq from 0 to len(nums) - 1
        # choose how many elements in sequence will have that value
        @cache
        def dfs(m, k, i, carry):
            if m < 0 or k < 0 or m + (carry.bit_count()) < k: return 0
            if m == 0:
                if carry.bit_count() == k: return 1
                return 0
            if i >= len(nums): return 0
            result = 0
            for c in range(m+1):
                mul = comb(m, c) * pow(nums[i], c, MOD) % MOD
                f = c + carry
                result += mul * dfs(m-c, k-f%2, i+1, f >> 1)
            return result % MOD
        return dfs(m, k, 0, 0)
