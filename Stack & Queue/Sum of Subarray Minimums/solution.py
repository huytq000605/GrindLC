class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        stack = []
        next_lt = [n for _ in range(n)]
        prev_lte = [-1 for _ in range(n)]
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                next_lt[stack.pop()] = i
            if stack:
                prev_lte[i] = stack[-1]
            stack.append(i)

        result = 0
        for i in range(n):
            l, r = prev_lte[i], next_lt[i]
            result = (result + nums[i] * (r-i) * (i-l)) % MOD
        return result 
