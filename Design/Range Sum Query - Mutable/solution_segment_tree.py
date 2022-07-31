class SegmentTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.left, self.right = None, None

    def query(self, start, end):
        if start > self.end or end < self.start:
            return 0

        if start <= self.start and end >= self.end:
            return self.val

        self.down()
        return self.left.query(start, end) + self.right.query(start, end)

    def update(self, start, end, val):
        if start > self.end or end < self.start:
            return

        if start <= self.start and end >= self.end:
            self.val = val
            return

        self.down()
        self.left.update(start, end, val)
        self.right.update(start, end, val)
        self.val = self.left.val + self.right.val

    def down(self):
        if self.start < self.end:
            if not self.left:
                mid = self.start + (self.end - self.start) // 2
                self.left = SegmentTree(self.start, mid)
                self.right = SegmentTree(mid + 1, self.end)

class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(0, len(nums) - 1)
        for i, num in enumerate(nums):
            self.st.update(i, i, num)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
