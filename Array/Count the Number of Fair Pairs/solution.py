class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        def pair_lower(value):
            j = n-1
            result = 0
            for i in range(n):
                while i < j and nums[i] + nums[j] > value:
                    j -= 1
                if i >= j: return result
                result += j-i
            return result
        return pair_lower(upper) - pair_lower(lower-1)
            
            
