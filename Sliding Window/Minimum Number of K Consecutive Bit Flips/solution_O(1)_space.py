class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        result = 0
        flips = 0
        j = 0
        for i in range(len(nums)):
            while i - j >= k:
                flips -= nums[j] >= 2
                j += 1
            if (nums[i] + flips) % 2 == 0:
                if i + k - 1 >= len(nums): return -1
                flips += 1
                nums[i] += 2
                result += 1
        return result
         
