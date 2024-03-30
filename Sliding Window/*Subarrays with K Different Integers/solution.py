class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(k):
            counter = defaultdict(int)
            start, result = 0, 0
            for i, num in enumerate(nums):
                counter[num] += 1
                while len(counter) > k:
                    counter[nums[start]] -= 1
                    if not counter[nums[start]]: counter.pop(nums[start])
                    start += 1
                result += i - start + 1
            return result
        return at_most(k) - at_most(k-1)
