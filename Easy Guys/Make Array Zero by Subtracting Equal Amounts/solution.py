class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        return len(s)
