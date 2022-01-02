class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = Counter()
        result = 0
        for t in time:
            t %= 60
            if t == 0:
                result += seen[0]
            else:
                result += seen[60 - t]
            seen[t] += 1
        return result
