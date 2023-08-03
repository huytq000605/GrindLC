class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        def dfs(i):
            result.append([*cur])
            if i >= len(nums):
                return
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j+1)
                cur.pop()
        dfs(0)
        return result
