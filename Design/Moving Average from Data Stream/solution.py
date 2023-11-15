class MovingAverage:

    def __init__(self, size: int):
        self.n = size
        self.vals = deque()
        self.s = 0

    def next(self, val: int) -> float:
        self.vals.append(val)
        self.s += val
        if len(self.vals) > self.n:
            self.s -= self.vals.popleft()
        return self.s / len(self.vals)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
