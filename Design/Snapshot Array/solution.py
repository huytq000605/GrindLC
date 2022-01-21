class SnapshotArray:

    def __init__(self, length: int):
        self.ver = [[[0, 0]] for i in range(length)]
        self.version = 0

    def set(self, index: int, val: int) -> None:
        if self.ver[index][-1][1] == self.version:
            self.ver[index][-1][0] = val
        else:
            self.ver[index].append([val, self.version])
            
    def snap(self) -> int:
        self.version += 1
        return self.version - 1

    def get(self, index: int, snap_id: int) -> int:
        start = 0
        end = len(self.ver[index]) - 1
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if self.ver[index][mid][1] > snap_id:
                end = mid - 1
            else:
                start = mid
        return self.ver[index][start][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)