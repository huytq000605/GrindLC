class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start, end = min(nums), max(nums)
        
        def valid(mn):
            houses = 0
            i = 0
            while i < n:
                if nums[i] <= mn:
                    i += 1
                    houses += 1
                i += 1
            return houses >= k
        
        while start < end:
            mid = start + (end - start) // 2
            if valid(mid):
                end = mid
            else:
                start = mid + 1
        return start
        
