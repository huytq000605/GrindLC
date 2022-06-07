class SummaryRanges:

    def __init__(self):
        self.pq = []

    def addNum(self, val: int) -> None:
        heappush(self.pq, (val, val))

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        while self.pq:
            start, end = heappop(self.pq)
            if not intervals or intervals[-1][-1] + 1 < start:
                intervals.append((start, end))
            else:
                intervals[-1] = (intervals[-1][0], max(intervals[-1][1], end))
        self.pq = intervals
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()