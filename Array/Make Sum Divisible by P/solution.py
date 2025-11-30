class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        m = 0
        for num in nums:
            m = (m + num) % p
        seen = dict()
        seen[0] = -1
        s = 0
        result = len(nums)
        for i in range(len(nums)):
            s = (s + nums[i]) % p
            need = (s - m + p) % p
            seen[s] = i
            if need in seen:
                result = min(result, i - seen[need])
        if result == len(nums): return -1
        return result
