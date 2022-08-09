class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        nums = set(arr)
        MOD = 10**9 + 7
        @cache
        def dfs(num):
            nonlocal nums
            result = 1
            for factor in nums:
                if num % factor == 0 and num // factor in nums:
                    result += dfs(factor) * dfs(num // factor)
            return result % MOD
        result = 0
        for num in arr:
            result += dfs(num)
            result %= MOD
        return result  
