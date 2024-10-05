class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n = len(nums)
        idxs = []
        for i in range(n):
            if nums[i]:
                idxs.append(i)
        if len(idxs) == 0:
            return 0
        result = 1
        MOD = 10**9 + 7
        for i in range(len(idxs) - 1):
            i1, i2 = idxs[i], idxs[i+1]
            result = (result * (i2 - i1)) % MOD
        return result
            
