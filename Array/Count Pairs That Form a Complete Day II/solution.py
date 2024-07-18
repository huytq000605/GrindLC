class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        seen = defaultdict(int)
        result = 0
        for h in hours:
            mod = h % 24
            result += seen[(24-mod)%24]
            seen[mod] += 1
        return result
