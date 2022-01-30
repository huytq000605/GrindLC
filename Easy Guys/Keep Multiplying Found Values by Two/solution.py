class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        counter = Counter(nums)
        while counter[original] > 0:
            original *= 2
        return original