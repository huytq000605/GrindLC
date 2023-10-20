class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        result = 0
        start = 0
        for i, c in enumerate(s):
            counter[c] += 1
            while len(counter) > k:
                counter[s[start]] -= 1
                if counter[s[start]] == 0: del counter[s[start]]
                start += 1
            result = max(result, i - start + 1)
        return result
