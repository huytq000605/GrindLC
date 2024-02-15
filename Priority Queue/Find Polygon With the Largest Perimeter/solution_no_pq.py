class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        k = 0
        s = 0
        result = -1
        for num in nums:
            s += num
            k += 1
            if s - num > num and k > 2:
                result = max(result, s)
        return result
