class FenwickTree:
    def __init__(self, size):
        self.bit = [0 for i in range(size + 1)]
        self.n = size

    def update(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0: 
            result += self.bit[idx]
            idx -= idx & -idx
        return result

    def range_sum(self, left, right):
        return self.query(right) - self.query(left - 1)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = FenwickTree(len(nums))
        for i, num in enumerate(nums):
            self.bit.update(i+1, num)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.bit.update(index+1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.range_sum(left+1, right+1)      


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
