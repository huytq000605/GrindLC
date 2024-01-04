class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        # set1: 1,4,9,16,...
        # set2: 2,8,18,32...
        # set3: 3,12,27,48,...
        # same_set[i] / same_set[1] = i*i (1-indexed)
        for i in range(n):
            v = i + 1
            k = 1
            res = 0
            while v*k*k-1 < n:
                res += nums[v * k * k - 1]
                k += 1
            result = max(result, res)
        return result




