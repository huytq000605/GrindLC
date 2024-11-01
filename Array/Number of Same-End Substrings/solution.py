class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        counters = [[0 for _ in range(26)] for _ in range(len(s))]
        for i in range(len(s)):
            if i: counters[i] = counters[i-1].copy()
            counters[i][ord(s[i]) - ord('a')] += 1
        result = []
        for a, b in queries:
            res = 0
            for c in range(26):
                n = counters[b][c] - (counters[a-1][c] if a else 0)
                res += n*(n+1)//2
            result.append(res)
        return result 
