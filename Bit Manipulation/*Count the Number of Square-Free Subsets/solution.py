class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        MOD = 10**9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        dp = [0 for _ in range(1 << 10)]
        
        for num in nums:
            mask = 0
            for i, prime in enumerate(primes):
                if num % (prime * prime) == 0:
                    mask = -1
                    break
                if num % prime == 0:
                    mask |= (1<<i)
            if mask > -1:
                for prev_mask in range(1<<10):
                    if mask & prev_mask == 0:
                        dp[mask | prev_mask] += dp[prev_mask]
                dp[mask] += 1
        
        return sum(dp) % MOD
                
                
                
