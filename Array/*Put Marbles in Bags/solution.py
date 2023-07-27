class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k >= n: return 0
        # k means we choose k-1 split points
        split = sorted([weights[i] + weights[i+1] for i in range(n-1)])
        result = 0
        for i in range(k-1):
            result += split[n-2-i] - split[i]
        return result
