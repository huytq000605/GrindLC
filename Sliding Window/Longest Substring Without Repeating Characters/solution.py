class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        start = 0
        result = 0
        for i, l in enumerate(s):
            while l in freq:
                freq.remove(s[start])
                start += 1
            result = max(result, i - start + 1)
            freq.add(l)
        return result