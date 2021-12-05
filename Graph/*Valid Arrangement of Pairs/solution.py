from collections import defaultdict, Counter
from typing import *

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        startWith = defaultdict(list)
        freqStart, freqEnd = Counter(), Counter()
        for start, end in pairs:
            startWith[start].append(end)
            freqStart[start] += 1
            freqEnd[end] += 1
        
        starting = pairs[0][0]
        for start, end in pairs:
            if freqStart[start] - freqEnd[start] == 1:
                starting = start
                break
        result = []
        def dfs(start):
            nonlocal result
            while startWith[start]:
                nextStart = startWith[start].pop()
                dfs(nextStart)
                result.append([start, nextStart])
        dfs(starting)
        return result[::-1]