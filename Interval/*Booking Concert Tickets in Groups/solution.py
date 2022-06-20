class SegmentTree:
    def __init__(self, start, end, m):
        self.start = start
        self.end = end
        self.max_range = m
        self.sum_range = m
        if self.start != self.end:
            self.mid = self.start + (self.end - self.start) // 2
            self.left = SegmentTree(self.start, self.mid, m)
            self.right = SegmentTree(self.mid+1, self.end, m)
            self.sum_range = self.left.sum_range + self.right.sum_range

    def query_max_range(self, end, value):
        # Early termination
        if self.start > end:
            return -1
        if self.start == self.end:
            if self.max_range >= value:
                return self.start
            return -1
        # Lazy query
        if self.left.max_range >= value:
            return self.left.query_max_range(end, value)
        return self.right.query_max_range(end, value)
    
    def query_sum_range(self, end, value):
        if self.start > end:
            return 0
        if self.end <= end:
            return self.sum_range
        return self.left.query_sum_range(end, value) + self.right.query_sum_range(end, value)
        
    # Log(n) update
    def update(self, idx, value):
        if self.start == self.end:
            if self.start == idx:
                self.max_range -= value
                self.sum_range -= value
            return
        if idx > self.mid:
            self.right.update(idx, value)
        else:
            self.left.update(idx, value)
        self.max_range = max(self.left.max_range, self.right.max_range)
        self.sum_range = self.left.sum_range + self.right.sum_range


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.st = SegmentTree(0, n-1, m)
        self.count = [m for i in range(n)]
        self.m = m
        self.idx = 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self.st.query_max_range(maxRow, k)
        if row == -1:
            return []
        self.st.update(row, k)
        self.count[row] -= k
        return [row, self.m - self.count[row] - k]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.st.query_sum_range(maxRow, k) >= k:
            while k > 0:
                if self.count[self.idx] > k:
                    self.st.update(self.idx, k)
                    self.count[self.idx] -= k
                    k = 0
                else:
                    self.st.update(self.idx, self.count[self.idx])
                    k -= self.count[self.idx]
                    self.count[self.idx] = 0
                    self.idx += 1
            return True
        else:
            return False
        


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)