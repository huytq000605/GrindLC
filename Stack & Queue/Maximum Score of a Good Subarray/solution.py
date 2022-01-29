class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        stack = []
        nums.append(0)
        n = len(nums)
        result = 0
        for j in range(n):
            while len(stack) > 0 and nums[stack[-1]] > nums[j]:
                value = nums[stack.pop()]
                if j - 1 >= k:
                    if len(stack) > 0:
                        if stack[-1] + 1 <= k:
                            width = j - stack[-1] - 1
                        else:
                            continue
                    else:
                        width = j
                    result = max(result, value * width)
            stack.append(j)
        return result
