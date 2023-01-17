class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter()
        start = 0
        result = 0
        pairs = 0
        for i, num in enumerate(nums):
            pairs += counter[num]
            counter[num] += 1
            while pairs - (counter[nums[start]] - 1) >= k:
                pairs -= (counter[nums[start]] - 1)
                counter[nums[start]] -= 1
                start += 1
            if pairs >= k:
                result += start + 1
        return result
