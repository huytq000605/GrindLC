class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start = 0
        have = defaultdict(int)
        result = 0
        def invalid(num):
            for k in have.keys():
                if abs(num - k) > 2:
                    return True
            return False
                
        for i, num in enumerate(nums):
            while invalid(num):
                have[nums[start]] -= 1
                if have[nums[start]] == 0:
                    have.pop(nums[start])
                start += 1
            
            size = i - start + 1
            result += size
            have[num] += 1
        return result
            
