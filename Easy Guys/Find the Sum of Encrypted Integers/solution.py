class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            mx = 0
            l = 0
            while num:
                mx = max(mx, num % 10)
                num //= 10
                l += 1
            encrypted = 0
            while l:
                encrypted = encrypted * 10 + mx
                l -= 1
            result += encrypted
        return result
