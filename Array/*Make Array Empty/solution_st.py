class SegmentTree:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None
    
    def query(self, start, end):
        if end < self.start or start > self.end:
            return 0
        if start <= self.start and self.end <= end:
            return self.val
        self.down()
        return self.left.query(start, end) + self.right.query(start, end)
    
    def update(self, start, end, val):
        if end < self.start or start > self.end:
            return
        if start <= self.start and self.end <= end:
            self.val = val
            return
        self.down()
        self.left.update(start, end, val)
        self.right.update(start, end, val)
        self.val = self.left.val + self.right.val
        
    def down(self):
        if self.start != self.end and not self.left:
            mid = self.start + (self.end - self.start) // 2
            self.left = SegmentTree(self.start, mid, 0)
            self.right = SegmentTree(mid + 1, self.end, 0)
        
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        
        st = SegmentTree(0, n-1, 0)
        for i in range(n):
            st.update(i, i, 1)
        
        prev = 0
        result = 0
        for num, idx in nums:
            if prev == idx:
                result += 1
            elif prev < idx:
                result += st.query(prev, idx-1) + 1
            else:
                result += st.query(prev, n-1) + st.query(0, idx-1) + 1
            st.update(idx, idx, 0)
            prev = idx
        return result
            
