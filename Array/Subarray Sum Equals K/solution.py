class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = dict()
        seen[0] = 1
        total = 0
        result = 0
        for num in nums:
            total += num
            if total - k in seen:
                result += seen[total - k]
            seen[total] = seen.get(total, 0) + 1
            
        return result
