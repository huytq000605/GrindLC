class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def ways(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0
            result = ways(i+1)
            if i + 1 < n and int(s[i:i+2]) <= 26:
                result += ways(i+2)
            return result
        return ways(0)
