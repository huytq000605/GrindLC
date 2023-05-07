class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        prefix = set()
        suffix = Counter(nums)
        for i, num in enumerate(nums):
            suffix[num] -= 1
            if suffix[num] == 0:
                suffix.pop(num)
            prefix.add(num)
            result[i] = len(prefix) - len(suffix)
        return result
