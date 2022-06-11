class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        result = n+1
        
        seen_prefix = dict()
        
        prefix = 0
        seen_prefix[0] = 0
        for i in range(n):
            prefix += nums[i]
            if prefix == x:
                result = min(result, i + 1)
            seen_prefix[prefix] = i + 1
            
        suffix = 0
        for i in range(n-1, -1, -1):
            suffix += nums[i]
            if x - suffix in seen_prefix:
                result = min(result, seen_prefix[x-suffix] + (n-i))
                
        if result > n:
            return -1
        return result
