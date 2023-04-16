class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        MOD = 10**9 + 7
        freq = [[0 for _ in range(26)] for _ in range(n)]
        for i in range(n):
            for word in words:
                c = ord(word[i]) - ord('a')
                freq[i][c] += 1
        @cache
        def dfs(i, j):
            if j >= len(target): return 1
            if i >= n: return 0
            result = dfs(i + 1, j)
            result += freq[i][ord(target[j]) - ord('a')] * dfs(i+1, j+1)
            return result % MOD
        return dfs(0, 0)
