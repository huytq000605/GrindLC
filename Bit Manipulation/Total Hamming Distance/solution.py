class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        arr = [0] * 32
        n = len(nums)
        for num in nums:
            for i in range(32):
                arr[i] += (num >> i) & 1
        result = 0
        for i in range(32):
            result += (n - arr[i]) * (arr[i])
        return result