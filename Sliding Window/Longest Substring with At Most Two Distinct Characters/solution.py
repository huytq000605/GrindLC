class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        j = 0
        d = defaultdict(int)
        result = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while len(d) > 2:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    d.pop(s[j])
                j += 1
            result = max(result, i - j + 1)
        return result
