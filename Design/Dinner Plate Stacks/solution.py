class DinnerPlates:
    def __init__(self, capacity: int):
        length = math.ceil(2*(10**5) / (capacity))
        self.capacity = capacity
        self.stacks = [[] for i in range(length)]
        self.left_most = [i for i in range(length)]
        self.right_most = []
        self.in_right = set()

    def push(self, val: int) -> None:
        idx = self.left_most[0]
        self.stacks[idx].append(val)
        if len(self.stacks[idx]) == self.capacity:
            heappop(self.left_most)
        if idx not in self.in_right:
            heappush(self.right_most, -idx)
            self.in_right.add(idx)
            
    def pop(self) -> int:
        while len(self.right_most) > 0:
            idx = -self.right_most[0]
            if len(self.stacks[idx]) == 0:
                heappop(self.right_most)
                self.in_right.discard(idx)
                continue
            elif len(self.stacks[idx]) == 1:
                heappop(self.right_most)
                self.in_right.discard(idx)
           if len(self.stacks[idx]) == self.capacity:
                heappush(self.left_most, idx)
            return self.stacks[idx].pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if len(self.stacks[index]) == 0:
            return -1
        else:
            if len(self.stacks[index]) == self.capacity:
                heappush(self.left_most, index)
            if len(self.stacks[index]) == 1:
                self.in_right.discard(index)
            return self.stacks[index].pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index) 
