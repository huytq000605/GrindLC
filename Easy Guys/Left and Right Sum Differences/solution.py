class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)
        pref = 0
        result = [0 for _ in range(n)]
        for i, num in enumerate(nums):
            result[i] = abs(s - pref - num - pref)
            pref += num
        return result
