class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(start):
            if start == n:
                return 0
            cur, res = 0, 0
            for i in range(start+1, n):
                if s[i] == s[start+cur]:
                    cur += 1
                else:
                    cur = 0
                    # Check with start again
                    if s[i] == s[start]:
                        cur = 1
                
                if (i - start + 1) % 2 == 0 and (i - start + 1) // 2 == cur:
                    res = max(res, dfs(start + cur) + 1)
                    cur = 0
            return max(res, 1)
        return dfs(0)
