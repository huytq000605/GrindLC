class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = 0
        seen = set()
        start = 0
        total = 0
        for num in nums:
            while num in seen:
                total -= nums[start]
                seen.discard(nums[start])
                start += 1
            total += num
            seen.add(num)
            result = max(result, total)
        return result
