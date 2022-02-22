class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
				# Use mask to represent idx in nums
        @cache
        def dfs(mask, slot, ith):
            if slot >= numSlots:
                return 0
            arr = []
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    arr.append(i)
                    
            result = dfs(mask, slot + 1, 0)
            if ith < 2:
                for i in range(len(arr)):
                    next_mask = mask | (1 << arr[i])
                    result = max(result, (nums[arr[i]] & (slot + 1)) + dfs(next_mask, slot, ith + 1) )
            return result
        return dfs(0, 0, 0)