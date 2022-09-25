class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.len = 0
        self.cap = k
        self.head = Node(-1)
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.len == self.cap:
            return False
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if not self.head.next:
            return False
        if self.head.next == self.tail:
            self.tail = self.head
        self.head.next = self.head.next.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if not self.head.next:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.head.next == None

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
