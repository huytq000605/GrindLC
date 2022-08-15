class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i]
        # nums[i] - i != nums[j] - j
        # Count good pairs
        # All pairs = n * (n-1) // 2
        n = len(nums)
        all_pairs = n * (n-1) // 2
        good_pairs = 0
        seen = defaultdict(int)
        for idx, num in enumerate(nums):
            if num - idx in seen:
                good_pairs += seen[num-idx]
            seen[num-idx] += 1
        return all_pairs - good_pairs
