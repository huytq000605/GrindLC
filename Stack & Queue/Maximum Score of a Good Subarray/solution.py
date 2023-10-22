class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(-math.inf)
        n = len(nums)
        stack = []
        result = 0
        for idx in range(n):
            while stack and nums[idx] < nums[stack[-1]]:
                j = idx - 1
                val = nums[stack.pop()]
                i = 0
                if stack:
                    i = stack[-1] + 1
                if i <= k and j >= k:
                    result = max(result, (j - i + 1) * val)
            stack.append(idx)
        return result
