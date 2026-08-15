class ST:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0 for _ in range(4 * self.n)]
        def build(i, tl, tr):
            if tl == tr:
                self.tree[i] = nums[tl]
                return self.tree[i]
            tm = tl + (tr - tl) // 2
            l = build(i*2+1, tl, tm)
            r = build(i*2+2, tm+1, tr)
            self.tree[i] = l + r
            return l + r 
        build(0, 0, self.n-1)
    
    def query(self, l, r, i = 0, tl = 0, tr = None):
        if tr == None: tr = self.n-1
        if r < tl or l > tr:
            return 0
        if l <= tl and r >= tr:
            return self.tree[i]
        tm = tl + (tr - tl) // 2
        return self.query(l, r, i*2+1, tl, tm) + self.query(l, r, i*2+2, tm+1, tr)
    
    def update(self, i, v, ti = 0, tl = 0, tr = None):
        if tr == None: tr = self.n-1
        if i < tl or i > tr:
            return self.tree[ti]
        if i == tl and tl == tr:
            self.tree[ti] = v
            return v
        tm = tl + (tr - tl) // 2
        l = self.update(i, v, ti*2+1, tl, tm)
        r = self.update(i, v, ti*2+2, tm+1, tr)
        self.tree[ti] = l + r
        return l + r
    

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        self.sts = [ST(matrix[r]) for r in range(m)]

    def update(self, row: int, col: int, val: int) -> None:
        self.sts[row].update(col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for r in range(row1, row2+1):
            result += self.sts[r].query(col1, col2)
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
