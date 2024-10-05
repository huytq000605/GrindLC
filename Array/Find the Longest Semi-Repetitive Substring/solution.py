class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        result = 1
        # start store the value we should count from
        start = 0
        # i store the last pair we met
        i, j = 0, 1
        while j < n:
            if s[j] == s[j-1]:
                # start should only change when we already got a pair
                if i > 0: start = i
                i = j
            result = max(result, j - start + 1)
            j += 1
        return result
