from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxValue = values[0]
        idxMaxValue = 0
        result = 0
        for idx, value in enumerate(values):
            if idx == 0: continue
            result = max(result, value + maxValue + idxMaxValue - idx)
            if value - maxValue + idx - idxMaxValue > 0:
                maxValue = value
                idxMaxValue = idx
        return result