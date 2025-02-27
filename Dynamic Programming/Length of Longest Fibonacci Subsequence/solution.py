class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(dict)
        result = 0
        for i in range(len(arr)):
            for j in range(i):
                c, b, a = arr[i], arr[j], arr[i] - arr[j]
                if a not in dp[b]: dp[c][b] = 1
                else: dp[c][b] = dp[b][a] + 1
                result = max(dp[c][b], result)
        return result + 1 if result > 1 else 0
