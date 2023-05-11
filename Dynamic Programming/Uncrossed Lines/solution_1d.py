class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if n > m:
            A, B = B, A
            m, n = n, m
        dp = [0 for _ in range(n+1)]
        # prev = [0 for _ in range(n+1)]
        for i in range(m):
            prev = 0
            for j in range(n):
                # if A[i] == B[j]:
                #   dp[j+1] = prev[j] + 1
                # else:
                #   dp[j+1] = max(dp[j+1], dp[j])
                # prev = dp[:]
                cur = dp[j+1]
                if A[i] == B[j]:
                    dp[j+1] = prev + 1
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                prev = cur
        return dp[-1]
