class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        prev = -math.inf
        result = 0
        for s, e in pairs:
            if s > prev:
                prev = e
                result += 1
            else:
                prev = min(e, prev)
        return result
