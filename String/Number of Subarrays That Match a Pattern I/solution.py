class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        result = 0
        for i in range(n-m):
            j = 0
            match = True
            for j in range(m):
                if pattern[j] == 0 and nums[i+j+1] != nums[i+j]:
                    match = False
                    break
                if pattern[j] != 0 and pattern[j] * (nums[i+j+1] - nums[i+j]) <= 0:
                    match = False
                    break
            if match:
                result += 1
        return result
            
