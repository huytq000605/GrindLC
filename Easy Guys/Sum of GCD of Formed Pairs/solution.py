class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        prefix_gcd = []
        for num in nums:
            mx = max(num, mx)
            prefix_gcd.append(math.gcd(num, mx))
        prefix_gcd.sort()
        n = len(nums)
        result = 0
        for i in range(n // 2):
            result += math.gcd(prefix_gcd[i], prefix_gcd[n-1-i])
        return result
