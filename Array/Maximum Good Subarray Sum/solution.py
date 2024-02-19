class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pos = dict()
        n = len(nums)
        result = -math.inf
        prefix = [0 for _ in range(n+1)]
        for i, num in enumerate(nums):
            if i > 0:
                prefix[i+1] = prefix[i]
            prefix[i+1] += num
            
            if num-k in pos:
                result = max(result, prefix[i+1] - prefix[pos[num-k]])
            
            if num+k in pos:
                result = max(result, prefix[i+1] - prefix[pos[num+k]])
            
            if num not in pos or prefix[i] - prefix[pos[num]] < 0:
                pos[num] = i
        
        if result == -math.inf:
            return 0
        return result
