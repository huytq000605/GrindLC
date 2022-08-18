class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        seen = dict()
        day = 1
        for task in tasks:
            if task in seen and seen[task] > day:
                day = seen[task]
            day += 1
            seen[task] = day + space
        return day - 1
