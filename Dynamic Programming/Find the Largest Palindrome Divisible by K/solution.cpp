class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        @cache
        def dfs(i, s):
            if i >= (n+1) // 2:
                if s == 0: return True
                return False
            for d in range(9, -1, -1):
                ns = s + d * pow(10, i, k) + d * pow(10, n-1-i, k)
                if n % 2 == 1 and i == n // 2: ns -= d * pow(10, n-1-i, k)
                if dfs(i+1, ns % k): return True
            return False
        s = 0
        result = ""
        for i in range((n+1) // 2):
            for d in range(9, -1, -1):
                ns = (s + d * pow(10, i, k) + d * pow(10, n-1-i, k))
                if n % 2 == 1 and i == n // 2: ns -= d * pow(10, n-1-i, k)
                ns %= k
                if dfs(i + 1, ns):
                    s = ns
                    result += str(d)
                    break
        if n % 2 == 1:
            return result + result[:-1][::-1]
        return result + result[::-1]
