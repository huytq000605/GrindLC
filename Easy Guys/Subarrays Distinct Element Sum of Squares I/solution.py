class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i, n):
                s = set()
                for k in range(i, j+1):
                    s.add(nums[k])
                result += len(s) ** 2
        return result
