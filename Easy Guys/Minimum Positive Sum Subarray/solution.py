class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = math.inf
        for k in range(l, r + 1):
            s = 0
            for i in range(len(nums)):
                if i >= k:
                    s -= nums[i-k]
                s += nums[i]
                if i >= k-1 and s > 0: result = min(result, s)
        if result == math.inf: return -1
        return result
