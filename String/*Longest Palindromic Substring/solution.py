class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""
        def extend(start, end):
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            return start + 1, end - 1

        for i in range(n):
            start, end = extend(i, i)
            if end - start + 1 > len(result):
                result = s[start:end+1]

            start, end = extend(i, i + 1)
            if end - start + 1 > len(result):
                result = s[start:end+1]
        return result

