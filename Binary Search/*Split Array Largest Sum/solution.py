class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def valid(value):
            group = 0
            curr = 0
            for num in nums:
                if curr + num > value:
                    group += 1
                    curr = 0
                    if group == m:
                        return False
                curr += num
            return True
            
            
        start = max(0, *nums)
        end = sum(nums)
        while start < end:
            value = start + (end - start) // 2
            if valid(value):
                end = value
            else:
                start = value + 1
        return start