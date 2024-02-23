class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups_by_mod = [[] for _ in range(k)]
        for num in nums:
            groups_by_mod[num % k].append(num)
        i = 0
        mod = 0
        while i < len(nums):
            while not groups_by_mod[mod]:
                mod += 1
            nums[i] = groups_by_mod[mod].pop()
            i += 1
        
        n = len(nums)
        @cache
        def dfs(i, j):
            if i >= n:
                if j == -1: return 0
                return 1
            result = dfs(i+1, j)
            if j == -1 or nums[j] - nums[i] != k:
                result += dfs(i+1, i)
            return result
        return dfs(0, -1)
