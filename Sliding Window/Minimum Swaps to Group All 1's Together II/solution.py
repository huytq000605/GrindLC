class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
        result = n    
        start = 0
        length = 0
        for i in range(ones):
            if nums[i] == 1:
                length += 1
        result = min(result, ones - length)
        
        for i in range(ones, 2*n):
            i = i%n
            if nums[start] == 1:
                length -= 1
            if nums[i] == 1:
                length += 1
            start += 1
            start %= n
            result = min(result, ones - length)
        return result