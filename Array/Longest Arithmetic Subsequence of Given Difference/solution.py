class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = defaultdict(int)
        result = 0
        for num in arr:
            d[num] = d[num-difference] + 1
            result = max(result, d[num])
        return result
