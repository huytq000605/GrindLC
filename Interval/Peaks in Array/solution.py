class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(4*n)]
    
    def query(self, start, end, idx = 0, left = 0, right = -1):
        if right == -1: right = self.n-1
        if end < left or start > right:
            return 0
        if start <= left and right <= end:
            return self.tree[idx]
        mid = left + (right - left) // 2
        return self.query(start, end, idx * 2 + 1, left, mid) + self.query(start, end, idx * 2 + 2, mid + 1, right)
    
    def update(self, start, end, value, idx = 0, left = 0, right = -1):
        if right == -1: right = self.n-1
        if end < left or start > right:
            return
        if start <= left and right <= end:
            self.tree[idx] = value
            return
        mid = left + (right - left) // 2
        self.update(start, end, value, idx * 2 + 1, left, mid)
        self.update(start, end, value, idx * 2 + 2, mid + 1, right)
        self.tree[idx] = self.tree[idx * 2 + 1] + self.tree[idx*2 + 2]
                
        

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(n)
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                st.update(i, i, 1)
                
        result = []
        for q, u, v in queries:
            if q == 1:
                result.append(st.query(u+1, v-1))
            else:
                nums[u] = v
                for i in range(max(0, u-1), min(n, u+2)):
                    if i in [0, n-1]: continue
                    if nums[i] > nums[i+1] and nums[i] > nums[i-1]: st.update(i, i, 1)
                    else: st.update(i, i, 0)
        
        return result
        
