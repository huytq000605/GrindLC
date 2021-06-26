from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modMap = [0] * 60
        result = 0
        for t in time:
            modMap[t%60] += 1
        for i in range(31):
            if i == 30 or i == 0:
                result += modMap[i] * (modMap[i] - 1) / 2
            else:
                result += modMap[i] * modMap[60-i]
        return int(result)