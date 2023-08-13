class Solution:
    def maxSum(self, nums: List[int]) -> int:
        result = -1
        n = len(nums)
        
        def max_digit(num):
            mx = -1
            for d in str(num):
                mx = max(mx, int(d))
            return mx
        
        for i in range(n):
            for j in range(i+1, n):
                num1, num2 = nums[i], nums[j]
                if max_digit(num1) == max_digit(num2):
                    result = max(result, num1 + num2)
        return result
