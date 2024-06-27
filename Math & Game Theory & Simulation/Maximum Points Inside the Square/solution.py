class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        points = [(max(abs(points[i][0]), abs(points[i][1])), s[i]) for i in range(len(s))]
        tags = defaultdict(lambda: 10**9+1)
        discard = math.inf
        for p, t in points:
            if tags[t] <= p:
                discard = min(discard, p)
            else:
                discard = min(discard, tags[t])
                tags[t] = p
        result = 0
        for p, t in points:
            if p < discard:
                result += 1
        return result
