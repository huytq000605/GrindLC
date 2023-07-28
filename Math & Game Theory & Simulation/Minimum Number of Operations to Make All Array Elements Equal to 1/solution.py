class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones: return n - ones
        result = math.inf
        for i in range(n):
            gcd = nums[i]
            for j in range(i+1, n):
                gcd = math.gcd(gcd, nums[j])
                if gcd == 1:
                    result = min(result, j - i - 1 + n)
        if result == math.inf: return -1
        return result
            
