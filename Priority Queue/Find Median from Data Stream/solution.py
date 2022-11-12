class MedianFinder:

    def __init__(self):
        self.larger = []
        self.smaller = []

    def addNum(self, num: int) -> None:
        n = len(self.larger) + len(self.smaller)
        if n % 2 == 0:
            heappush(self.smaller, -num)
            heappush(self.larger, -heappop(self.smaller))
        else:
            heappush(self.larger, num)
            heappush(self.smaller, -heappop(self.larger))

    def findMedian(self) -> float:
        n = len(self.larger) + len(self.smaller)
        if n % 2 == 0:
            return (self.larger[0] - self.smaller[0]) / 2
        else:
            return self.larger[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
