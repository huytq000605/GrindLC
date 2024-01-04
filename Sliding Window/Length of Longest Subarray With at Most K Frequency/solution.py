class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        start = 0
        result = 0
        for i, num in enumerate(nums):
            counter[num] += 1
            while counter[num] > k:
                counter[nums[start]] -= 1
                start += 1
            result = max(result, i - start + 1)
        return result
