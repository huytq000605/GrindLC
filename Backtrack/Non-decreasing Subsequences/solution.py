class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        def dfs(i):
            if len(path) > 1:
                result.append([*path])
            used = set()
            for j in range(i, n):
                if nums[j] in used: continue
                if not path or path[-1] <= nums[j]:
                    used.add(nums[j])
                    path.append(nums[j])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return result
