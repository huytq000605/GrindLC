class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        result = 0
        for g in gain:
            s += g
            result = max(result, s)
        return result
