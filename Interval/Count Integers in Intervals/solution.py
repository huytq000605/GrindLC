class SegmentTree:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None
    
    def update(self, start, end):
        if end < self.start or start > self.end:
            return
        
        if start <= self.start and end >= self.end:
            self.value = (self.end - self.start + 1)
            self.left = None
            self.right = None
            return

        self.down()
        self.left.update(start, end)
        self.right.update(start, end)
        self.value = self.left.value + self.right.value

    def down(self):
        if self.start != self.end:
            if not self.left:
                mid = self.start + (self.end - self.start) // 2
                self.left = SegmentTree(self.start, mid, 0)
                self.right = SegmentTree(mid + 1, self.end, 0)
        

class CountIntervals:

    def __init__(self):
        self.st = SegmentTree(0, 10**9, 0)

    def add(self, left: int, right: int) -> None:
        self.st.update(left, right)

    def count(self) -> int:
        return self.st.value


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()