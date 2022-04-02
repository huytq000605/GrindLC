class DinnerPlates:
    def __init__(self, capacity: int):
        self.stacks = []
        self.left_most = []
        self.capacity = capacity    
    
    def push(self, val: int) -> None:
        while (
            len(self.left_most) > 0 and
            self.left_most[0] < len(self.stacks) and
            len(self.stacks[self.left_most[0]]) == self.capacity
        ):
            heappop(self.left_most)
        
        if len(self.left_most) == 0:
            heappush(self.left_most, len(self.stacks))
        
        if self.left_most[0] == len(self.stacks):
            self.stacks.append([])
            
        self.stacks[self.left_most[0]].append(val)
            
            
        
    def pop(self) -> int:
        while len(self.stacks):
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
                continue
            if len(self.stacks[-1]) == self.capacity:
                heappush(self.left_most, len(self.stacks) - 1)
            return self.stacks[-1].pop()
        return -1
        
    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1
        else:
            if len(self.stacks[index]) == self.capacity:
                heappush(self.left_most, index)
            return self.stacks[index].pop()
                


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)