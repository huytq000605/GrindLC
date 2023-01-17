class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        remaining_ones = 0
        past_ones = 0
        n = len(s)
        for c in s:
            if c == "1": remaining_ones += 1
        result = min(remaining_ones, n-remaining_ones)
        for i, c in enumerate(s):
            if c == "1": 
                past_ones += 1
                remaining_ones -= 1
            remaining_zeros = n - 1 - i - remaining_ones
            result = min(result, past_ones + remaining_zeros)
        return result
