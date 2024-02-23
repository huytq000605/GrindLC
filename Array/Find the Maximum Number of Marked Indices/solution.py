class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # we should choose m first numbers if have m pairs
        # so that means maximum number of pairs is n//2
        # we choose nums[j] with j starting from n//2
        j = n//2
        result = 0
        for i in range(n//2):
            if j >= n: break
            while j < n and nums[i] * 2 > nums[j]:
                j += 1
            if j >= n: break
            result += 2
            j += 1
        return result
