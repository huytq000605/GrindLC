class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = Counter(nums)
        freq = sorted(counter.values(), reverse = True)[:10]
        n = len(quantity)
        
        sum_submask = [0 for i in range(1 << n)]
        for i in range(1 << n):
            for j in range(n):
                if (i >> j) & 1 == 1:
                    sum_submask[i] += quantity[j]
        
				# Assign subset of quantity to freq
        @cache
        def dfs(idx, mask):
            if mask == 0:
                return True
            if idx >= len(freq):
                return False
            submask = mask
            while submask > 0:
                if sum_submask[submask] <= freq[idx]:
                    if dfs(idx + 1, mask ^ submask):
                        return True
                submask = (submask - 1) & mask
            return False
        
        return dfs(0, (1<<n) - 1)