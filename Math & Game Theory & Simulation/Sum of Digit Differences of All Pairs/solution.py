class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digits = len(str(nums[0]))
        result = 0
        for _ in range(digits):
            counter = Counter()
            for i, num in enumerate(nums):
                digit = num % 10
                nums[i] //= 10
                counter[digit] += 1
            n = len(nums)
            for d in range(10):
                result += counter[d] * (n - counter[d])
                n -= counter[d]
        return result
