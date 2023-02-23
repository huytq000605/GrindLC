"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedules: '[[Interval]]') -> '[Interval]':
        pq = []
        for i, schedule in enumerate(schedules):
            heappush(pq, (schedule[0].start, schedule[0].end, i, 0))
        result = []
        last_end = -math.inf
        while pq:
            s, e, ith, idx = heappop(pq)
            idx += 1
            if idx < len(schedules[ith]):
                schedule = schedules[ith]
                heappush(pq, (schedule[idx].start, schedule[idx].end, ith, idx))
                
            if last_end < s and last_end != -math.inf:
                result.append(Interval(last_end, s))
            last_end = max(last_end, e)
        return result
