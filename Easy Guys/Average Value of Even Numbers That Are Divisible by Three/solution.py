class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, n = 0, 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                s += num
                n += 1
        if n == 0:
            return 0
        return s // n
