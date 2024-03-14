class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        # number of subarrays with sum <= k
        def at_most(k):
            if k < 0: return 0
            s = 0
            start = 0
            result = 0
            for i in range(n):
                s += nums[i]
                while s > k:
                    s -= nums[start]
                    start += 1
                result += i - start + 1
            return result
        
        return at_most(goal) - at_most(goal-1)
