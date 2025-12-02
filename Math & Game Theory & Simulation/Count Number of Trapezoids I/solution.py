class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ys = defaultdict(int)
        for [x, y] in points:
            ys[y] += 1
        result = 0
        total = 0
        for y, c in ys.items():
            lines = c * (c - 1) // 2
            result = (result + lines * total) % MOD
            total = (total + lines) % MOD
        return result
