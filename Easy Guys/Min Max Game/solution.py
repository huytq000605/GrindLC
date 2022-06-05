class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            n //= 2
            for i in range(n):
                if i % 2 == 0:
                    nums[i] = min(nums[i*2], nums[i*2+1])
                else:
                    nums[i] = max(nums[i*2], nums[i*2+1])
        return nums[0]