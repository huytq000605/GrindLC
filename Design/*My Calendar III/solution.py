class SegmentTree:
    def __init__(self, start, end, val = 0):
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.val, self.lazy = val, 0
        
    def query(self, start, end):
        if start <= self.start and end >= self.end:
            return self.val
        
        if start > self.end or end < self.start:
            return 0
        
        self.down()
        mid = self.start + (self.end - self.start) // 2
        return max(self.left.query(self.start, mid), self.right.query(mid + 1, self.end))
    
    def update(self, start, end, val):
        if start <= self.start and end >= self.end:
            self.lazy += val
            self.val += val
            return
        
        if start > self.end or end < self.start:
            return
        
        self.down()
        mid = self.start + (self.end - self.start) // 2
        self.left.update(start, end, val)
        self.right.update(start, end, val)
        self.val = max(self.left.val, self.right.val)
    
    def down(self):
        if self.start != self.end:
            if not self.left:
                mid = self.start + (self.end - self.start) // 2
                self.left = SegmentTree(self.start, mid, self.val)
                self.right = SegmentTree(mid + 1, self.end, self.val)
            elif self.lazy:
                self.left.val += self.lazy
                self.left.lazy += self.lazy
                self.right.val += self.lazy
                self.right.lazy += self.lazy
        self.lazy = 0

class MyCalendarThree:

    def __init__(self):
        self.st = SegmentTree(0, 10**9)

    def book(self, start: int, end: int) -> int:
        self.st.update(start, end-1, 1)
        return self.st.val


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
