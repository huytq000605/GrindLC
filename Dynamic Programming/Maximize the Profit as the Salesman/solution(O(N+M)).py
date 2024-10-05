class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        ends = defaultdict(list)
        for s, e, g in offers:
            ends[e].append((s, g))
        
        # dp[i] = maxium gold after first `i` offers
        dp = [0 for _ in range(n + 1)]
        result = 0
        for end in range(n):
            dp[end + 1] = dp[end]
            if end in ends:
                for s, g in ends[end]:
                    dp[end+1] = max(dp[end+1], dp[s] + g)
                    result = max(result, dp[end+1])
        return result
