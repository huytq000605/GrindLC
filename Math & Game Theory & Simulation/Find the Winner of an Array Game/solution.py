class Solution:
    def getWinner(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k >= n-1:
            return max(nums)
        streak = 0
        num = nums[0]
        for i in range(1, n):
            if num < nums[i]:
                streak = 0
                num = nums[i]
            streak += 1
            if streak >= k:
                return num
        return num
