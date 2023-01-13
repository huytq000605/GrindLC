class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.arr = [0 for i in range(n)]
        

    def allocate(self, size: int, mID: int) -> int:
        free = 0
        for i in range(self.n):
            if self.arr[i] == 0:
                free += 1
            else:
                free = 0
            if free == size:
                for j in range(i, i - size, -1):
                    self.arr[j] = mID
                return j
        return -1
        

    def free(self, mID: int) -> int:
        free = 0
        for i in range(self.n):
            if self.arr[i] == mID:
                self.arr[i] = 0
                free += 1
        return free


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
