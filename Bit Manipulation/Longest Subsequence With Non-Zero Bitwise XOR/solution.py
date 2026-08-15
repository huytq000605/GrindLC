class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        z = 0
        for num in nums: 
            xor ^= num
            z += num == 0
        if xor != 0: return n
        if n == z: return 0
        return n-1
