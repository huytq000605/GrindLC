class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums[0])
        for i in range(2**n):
            b = bin(i)[2:]
            b = "0" * (n - len(b)) + b
            if b not in s:
                return b
        return ""

