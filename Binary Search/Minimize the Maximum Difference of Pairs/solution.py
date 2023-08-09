class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        n = len(nums)
        def valid(threshold):
            i = 0
            k = 0
            while i < n:
                if i + 1 >= n: break
                if nums[i+1] - nums[i] > threshold:
                    i += 1
                    continue
                else:
                    i += 2
                    k += 1
            return k >= p
        
        while start < end:
            mid = start + (end - start) // 2
            if valid(mid):
                end = mid
            else:
                start = mid + 1
        return start
                    
                    
