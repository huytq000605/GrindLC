class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        result = []
        n = len(nums)
        def dfs(i):
            if i >= len(nums):
                result.append([*cur])
            for j in range(i, n):
                cur.append(nums[j])
                nums[j], nums[i] = nums[i], nums[j]
                dfs(i+1)
                nums[j], nums[i] = nums[i], nums[j]
                cur.pop()
        dfs(0)
        return result
