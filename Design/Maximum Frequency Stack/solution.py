class FreqStack:

    def __init__(self):
        self.heap = []
        self.idx = 0
        self.freq = Counter()

    def push(self, val: int) -> None:
        self.freq[val] += 1
        heappush(self.heap, (-self.freq[val], -self.idx, val))
        self.idx += 1

    def pop(self) -> int:
        val = heappop(self.heap)[2]
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()