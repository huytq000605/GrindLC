class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        start = 0
        end = nums[-1] - nums[0]
        while start < end:
            mid = start + (end - start) // 2
            count = 0
            
            i, j = 0, 0
            while i < n:
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
                i += 1
            
            if count < k:
                start = mid + 1
            else:
                end = mid
        return start