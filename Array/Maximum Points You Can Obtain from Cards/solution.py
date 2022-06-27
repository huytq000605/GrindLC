class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        target = n - k
        cur = 0
        min_subarray = math.inf
        for i in range(n):
            if i >= target:
                cur -= cardPoints[i-target]
            cur += cardPoints[i]
            if i >= target - 1:
                min_subarray = min(min_subarray, cur)
        return sum(cardPoints) - min_subarray
