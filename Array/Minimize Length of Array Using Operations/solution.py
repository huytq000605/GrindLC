class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mn = min(nums)
        # Smaller number can always eliminate bigger number
        # We care about if there is any 0 < x % y < mn

        # If there is x % mn = m, with 0 < m < mn -> return 1
        
        # Is there x % y < mn, x % mn = 0, y % mn = 0
        # But x % mn = 0 and y % mn = 0 -> x % y = 0
        for num in nums:
            if num % mn > 0 and num % mn < mn:
                return 1 
        return (nums.count(mn) + 1) // 2
