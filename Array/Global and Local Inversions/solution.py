class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        max_num = -math.inf
        for i in range(n):
            if i >= 2:
                max_num = max(max_num, nums[i-2])
            if max_num > nums[i]:
                return False
        return True
