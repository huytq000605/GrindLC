class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        

        prefix = [0 for _ in range(n+1)]
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        def valid(length):
            for start in range(n - length + 1):
                end = start + length - 1
                s = prefix[end+1] - prefix[start]
                mid = start + (end - start) // 2
                median = nums[start + (end - start) // 2]
                
                if median * (mid - start + 1) - (prefix[mid+1] - prefix[start])\
                    + prefix[end+1] - prefix[mid] - median * (end - mid + 1) <= k:
                    return True
            return False
        
        start = 1
        end = n
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if valid(mid):
                start = mid
            else:
                end = mid - 1
        return start
