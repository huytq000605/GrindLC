class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted([(ages[i], scores[i]) for i in range(n)])
        dp = [players[i][1] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)
