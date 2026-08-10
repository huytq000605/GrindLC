dp = [False for _ in range(10**5 + 1)]
for i in range(10**5+1):
    k = 1
    while k*k <= i:
        s = k*k
        if s > i: break
        if not dp[i-s]:
            dp[i] = True
            break
        k += 1

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dp[n]
