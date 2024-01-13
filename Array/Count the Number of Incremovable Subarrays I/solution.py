class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for start in range(n):
            for end in range(start, n):
                prev = 0
                valid = True
                for i in range(n):
                    if i >= start and i <= end: continue
                    if nums[i] <= prev:
                        valid = False
                        break
                    prev = nums[i]
                if valid:
                    result += 1
        return result
