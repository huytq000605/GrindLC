class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        result = 0
        current_flip = 0
        n = len(nums)
        for i in range(n):
            if i >= k and nums[i-k] >= 2:
                current_flip -= 1
            if i <= n - k:
                if (nums[i] == 0 and current_flip % 2 == 0) or (nums[i] == 1 and current_flip % 2 == 1):
                    result += 1
                    current_flip += 1
                    nums[i] += 2
            else:
                if (nums[i] == 0 and current_flip % 2 == 0) or (nums[i] == 1 and current_flip % 2 == 1):
                    return -1
        return result