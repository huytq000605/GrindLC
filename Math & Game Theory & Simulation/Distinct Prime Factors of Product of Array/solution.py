class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        for num in nums:
            factor = 2
            while num > 1:
                if num % factor == 0:
                    num //= factor
                    factors.add(factor)
                    continue
                factor += 1
        return len(factors)
