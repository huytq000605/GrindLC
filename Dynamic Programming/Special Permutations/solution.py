class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        @cache
        def dfs(j, mask):
            if mask == 2 ** n - 1:
                return 1
            result = 0
            for i in range(n):
                if (mask >> i) & 1: continue
                if nums[j] % nums[i] == 0 or nums[i] % nums[j] == 0:
                    result += dfs(i, mask | (1 << i))
                    result %= MOD
            return result
        
        result = 0
        for i in range(n):
            result += dfs(i, 1 << i)
            result %= MOD
        return result
                    
