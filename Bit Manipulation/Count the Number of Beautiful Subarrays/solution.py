class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        s = 0
        seen = defaultdict(int)
        result = 0
        seen[0] = 1
        for num in nums:
            s ^= num
            if s in seen:
                result += seen[s]
            seen[s] += 1
        return result
