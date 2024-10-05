class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i] lowest price when buying first i fruits
        dp = [0 for _ in range(n+1)]
        dq = deque()
    
        for i in range(n):
            # cannot buy fruits[i] for free
            while dq and (dq[0]+1) + (dq[0]+1) < i + 1:
                dq.popleft()
            # the deal in the queue is worse than the deal of buying this fruit
            while dq and dp[dq[-1]] + prices[dq[-1]] >= dp[i] + prices[i]:
                dq.pop()
            dq.append(i)
            dp[i+1] = dp[dq[0]] + prices[dq[0]]
        return dp[-1]
