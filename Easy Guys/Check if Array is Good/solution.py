class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        counter = Counter(nums)
        if len(nums) != n+1:
            return False
        for num in range(1, n):
            if counter[num] != 1:
                return False
        if counter[n] != 2:
            return False
        return True
