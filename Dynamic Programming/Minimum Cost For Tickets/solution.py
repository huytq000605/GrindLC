class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        # dp[i] = minimum cost to travel first i days in days
        dp = [math.inf for _ in range(n+1)]
        last_7 = deque()
        last_30 = deque()
        dp[0] = 0
        for i, d in enumerate(days):
            while last_7 and last_7[0][0] + 7 <= d: last_7.popleft()
            while last_30 and last_30[0][0] + 30 <= d: last_30.popleft()
            last_7.append((d, dp[i] + costs[1]))
            last_30.append((d, dp[i] + costs[2]))
            # (previous cost + 1-day ticket, bougth 7 days, bought 30 days)
            dp[i+1] = min(dp[i] + costs[0], last_7[0][1], last_30[0][1])
        return dp[-1]
