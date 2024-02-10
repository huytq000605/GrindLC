class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        result = []
        max_size = max(dp)
        for i in range(n-1, -1, -1):
            if dp[i] == max_size and (not result or result[-1] % nums[i] == 0):
                result.append(nums[i])
                max_size -= 1
                
        return result
                    
        
