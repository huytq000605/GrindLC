class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        last = dict()
        MOD = 10**9 + 7
        for i, num in enumerate(nums):
            last[num] = i
        nxt = dict()
        mx_idx = -1
        idxs = []
        for i, num in enumerate(nums):
            mx_idx = max(mx_idx, last[num])
            idxs.append(i)
            while i == mx_idx and idxs:
                nxt[idxs.pop()] = i + 1
        @cache
        def dfs(i):
            if i >= len(nums):
                return 1
            # merge this into previous or separate
            # if i == 0, nothing in previous to merge
            multiply = 2
            if i == 0: multiply = 1
            
            result = (dfs(nxt[i]) * multiply) % MOD
            return result
        return dfs(0) % MOD
            

