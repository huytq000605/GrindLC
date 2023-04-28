class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(num):
            if num <= 1: return False
            i = 2
            while i * i <= num:
                if num % i == 0: return False
                i += 1
            return True
        n = len(nums)
        result = 0
        for r in range(n):
            if is_prime(nums[r][r]):
                result = max(result, nums[r][r])
            if is_prime(nums[r][n-1-r]):
                result = max(result, nums[r][n-1-r])
        return result
            
