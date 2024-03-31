class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        negative = sorted([num for num in nums if num < 0])
        positive = [num for num in nums if num > 0]
        
        zeros = len(negative) + len(positive) != n
        
        if not negative and not positive:
            return 0
        
        if len(negative) % 2 == 1:
            num = negative.pop()
            if not negative and not positive:
                if zeros: return 0
                return num
        
        result = 1
        for p in positive:
            result *= p
        for n in negative:
            result *= n
        
        return result
            
