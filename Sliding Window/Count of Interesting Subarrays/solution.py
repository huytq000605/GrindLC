class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = defaultdict(int)
        acc = 0
        result = 0
        prefix[0] = 1
        for i, num in enumerate(nums):
            if num % modulo == k:
                acc = (acc + 1) % modulo
            prev = ((acc - k) % modulo + modulo) % modulo
            if prev in prefix:
                result += prefix[prev]
            prefix[acc] += 1
        return result
