class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set(nums)
        start = 0
        result = 0
        can_start = 0
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            while len(d) == len(s):
                can_start += 1
                d[nums[start]] -= 1
                if d[nums[start]] == 0:
                    del d[nums[start]]
                start += 1
            result += can_start
        return result
