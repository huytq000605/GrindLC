from collections import defaultdict, deque
from typing import *
from heapq import heappush, heappop

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = defaultdict(deque)
        need_dry = []
        for idx, rain in enumerate(rains):
            if rain > 0:
                lakes[rain].append(idx)
        result = []
        for idx, rain in enumerate(rains):
            if rain > 0:
                # If meet a lake need to be dry => return []
                if len(need_dry) > 0 and idx == need_dry[0]:
                    return []
                lakes[rain].popleft()
                # If have next idx => put into heap
                if len(lakes[rain]) > 0:
                    heappush(need_dry, lakes[rain][0])
                result.append(-1)
            else:
                if len(need_dry) > 0:
                    result.append(rains[heappop(need_dry)])
                else:
                    result.append(1)
        return result