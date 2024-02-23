class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        # dp[j] = how many triplets (i, j, k) with i < j < k and nums[i] < nums[k] < nums[j]
        dp = [0 for j in range(n)]
        for j in range(n):
            # number of num smaller than nums[j]
            prev_small = 0
            for i in range(j):
                # we have 2 things happen here
                # 1. increase prev_small
                # 2. quadruplets will be increased if nums[i] forms 132 pattern, nums[j] will be 4 in 1324
                if nums[i] < nums[j]:
                    result += dp[i]
                    prev_small += 1
                # nums[i] will be 132 pattern
                elif nums[i] > nums[j]:
                    dp[i] += prev_small
        return result
                    
