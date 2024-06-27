class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        idxs = {c: i for (i, c) in enumerate(s)}
        result = 0
        for i, c in enumerate(t):
            result += abs(i - idxs[c])
        return result
