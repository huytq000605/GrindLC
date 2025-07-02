class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        segments = []
        for c in word:
            if not segments or segments[-1][0] != c:
                segments.append([c, 1])
            else:
                segments[-1][1] += 1
        total = 1
        for c, f in segments:
            total = (total * f) % MOD
        if len(segments) >= k: return total
        dp = [0 for _ in range(k)]
        dp[0] = 1
        for c, f in segments:
            prefix = 0
            ndp = [0 for _ in range(k)]
            # ndp[i] = dp[i-t] for t in range(1, f+1)
            for i in range(1, k):
                prefix = (prefix + dp[i-1]) % MOD
                if i - f - 1 >= 0:
                    prefix = (prefix - dp[i-f-1] + MOD) % MOD
                ndp[i] = prefix
            dp = ndp
        invalid = 0
        for d in dp:
            invalid = (invalid + d) % MOD
        return (total - invalid + MOD) % MOD
