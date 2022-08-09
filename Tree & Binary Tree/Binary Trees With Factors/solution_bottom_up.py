class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        d = dict()
        nums = sorted(arr)
        result = 0
        MOD = 10**9 + 7
        for i in range(len(arr)):
            d[nums[i]] = 1
            for j in range(i):
                if nums[i] % nums[j] == 0 and nums[i] // nums[j] in d:
                    d[nums[i]] += d[nums[j]] * d[nums[i] // nums[j]]
                    d[nums[i]] %= MOD
        return sum(d.values()) % MOD
