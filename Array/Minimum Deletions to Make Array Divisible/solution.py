class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a, b):
            if b > a:
                a, b = b, a
            if b == 0:
                return a
            return gcd(b, a % b)
        g = numsDivide[0]
        for num in numsDivide:
            g = gcd(g, num)
        nums.sort()
        for i, num in enumerate(nums):
            if g % num == 0:
                return i
        return -1
