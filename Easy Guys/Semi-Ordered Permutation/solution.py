class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = -1, -1
        for i, num in enumerate(nums):
            if num == 1:
                a = i
            if num == n:
                b = i
        if a > b:
            return a-1 + n-1-b
        else:
            return a + n-1-b
