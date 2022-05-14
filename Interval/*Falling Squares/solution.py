class SegmentTree:
    def __init__(self, start, end, value = 0):
        self.start = start
        self.end = end
        self.value = value
        self.lazy = 0
        self.left = None
        self.right = None
    
    def query(self, start, end):
        if end < self.start or start > self.end:
            return 0
        
        if start <= self.start and end >= self.end:
            return self.value
        
        self.down()
        result = max(self.left.query(start, end), self.right.query(start, end))
        return result
    
    def update(self, start, end, value):
        if end < self.start or start > self.end:
            return
        
        if start <= self.start and end >= self.end:
            self.value = value
            self.lazy = value
            return

        self.down()
        self.left.update(start, end, value)
        self.right.update(start, end, value)
        self.value = max(self.left.value, self.right.value)

    def down(self):
        if self.start != self.end:
            if not self.left:
                mid = self.start + (self.end - self.start) // 2
                self.left = SegmentTree(self.start, mid, self.value)
                self.right = SegmentTree(mid + 1, self.end, self.value)
            elif self.lazy > 0: 
                self.left.value = self.lazy
                self.right.value = self.lazy
                self.left.lazy = self.right.lazy = self.lazy
        self.lazy = 0
        

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        st = SegmentTree(0, 10**14)
        result = []
        for s, w in positions:
            st.update(s, s + w - 1, st.query(s, s + w - 1) + w)
            result.append(st.value)
        return result