class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def lps(s):
            lps = [0 for _ in range(len(s))]
            j = 0
            for i in range(1, len(s)):
                while j and s[i] != s[j]:
                    j = lps[j-1]
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps
        
        needle_lps = lps(needle)
        j = 0
        for i in range(len(haystack)):
            while j and haystack[i] != needle[j]:
                j = needle_lps[j-1]
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle): return i - j + 1
        return -1
