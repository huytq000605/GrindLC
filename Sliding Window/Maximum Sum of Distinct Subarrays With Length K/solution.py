class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        n = len(nums)
        result = 0
        seen = set()
        s = 0
        for end in range(n):
            while nums[end] in seen or (end - start + 1) > k:
                s -= nums[start]
                seen.remove(nums[start])
                start += 1
            s += nums[end]
            seen.add(nums[end])
            if end - start + 1 == k:
                result = max(result, s)
        return result
