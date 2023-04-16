class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mx = 0
        result = math.inf
        for div in divisors:
            score = 0
            for num in nums:
                if num % div == 0:
                    score += 1
            if score >= mx:
                if score > mx:
                    result = div
                else:
                    result = min(result, div)
                mx = score
                
        return result
