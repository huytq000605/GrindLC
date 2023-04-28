class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        CAP = max(max(nums[row]) for row in range(n))
        is_prime = [True for _ in range(CAP + 1)]
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, CAP+1):
            if is_prime[i]:
                j = i*i
                while j <= CAP:
                    is_prime[j] = False
                    j += i
        n = len(nums)
        result = 0
        for r in range(n):
            if is_prime[nums[r][r]]:
                result = max(result, nums[r][r])
            if is_prime[nums[r][n-1-r]]:
                result = max(result, nums[r][n-1-r])
        return result
            
