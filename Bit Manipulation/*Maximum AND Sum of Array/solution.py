class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        
				# For each step, we use 2 bit to represent how many number are there in them
        @cache
        def dfs(idx, mask):
            if idx == n:
                return 0

            result = 0
            for slot in range(numSlots):
                if (mask >> (slot * 2 + 1)) & 1  == 1:
                    continue
                if (mask >> (slot * 2)) & 1 == 1:
                    next_mask = mask | (1 << (slot * 2 + 1))
                    result = max(result, dfs(idx + 1, next_mask) + (nums[idx] & (slot + 1)) )
                else:
                    next_mask = mask | (1 << (slot * 2))
                    result = max(result, dfs(idx + 1, next_mask) + (nums[idx] & (slot + 1)) )
            return result
    
        return dfs(0, 0)