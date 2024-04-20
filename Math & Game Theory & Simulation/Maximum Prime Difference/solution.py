class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(num):
            if num <= 1: return False
            i = 2
            while i * i <= num:
                if num % i == 0: return False
                i += 1
            return True
        
        p = -1
        result = 0
        for i in range(len(nums)):
            if is_prime(nums[i]):
                if p == -1:
                    p = i
                else:
                    result = i - p
        return result
