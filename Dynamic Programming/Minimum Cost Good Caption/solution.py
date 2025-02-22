class Solution:
    def minCostGoodCaption(self, s: str) -> str:
        n = len(s)
        if n < 3: return ""
        @cache
        def dfs(i, p1, length):
            if i >= n:
                if length >= 3: return 0
                return math.inf
            c = ord(s[i]) - ord('a')
            res = math.inf
            for nc in range(26):
                if length >= 3 or nc == p1 or length == 0:
                    ops = abs(c - nc)
                    nlength = min(3, length + 1) if p1 == nc else 1
                    res = min(res, ops + dfs(i+1, nc, nlength))
            return res
        
        min_ops = dfs(0, -1, 0)
        ops = 0
        length = 1
        result = "`"
        for i in range(n):
            p1 = ord(result[-1]) - ord('a')
            for c in range(26):
                if length >= 3 or c == p1 or p1 == -1:
                    cost = abs(c - (ord(s[i]) - ord('a')))
                    nlength = min(3, length + 1) if c == p1 else 1
                    if ops + cost + dfs(i+1, c, nlength) == min_ops:
                        result += chr(c + ord('a'))
                        ops += cost
                        length = nlength
                        break
        return result[1:]
