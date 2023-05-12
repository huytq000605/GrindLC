class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n= len(questions)
        dp = [0 for _ in range(n+1)]
        for i in reversed(range(n)):
            p, b = questions[i]
            dp[i] = max(dp[i+1], p + dp[min(n, i + b + 1)])
        return dp[0]
