class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.arr = [0 for _ in range(k)]
        self.head = 0
        self.tail = -1
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.len == self.cap: return False
        self.tail = (self.tail + 1) % self.cap
        self.arr[self.tail] = value
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len == 0: return False
        self.head = (self.head + 1) % self.cap
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.len == 0: return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.len == 0: return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
