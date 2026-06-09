class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree_max = [0 for _ in range(4*self.n)]
        self.tree_min = [0 for _ in range(4*self.n)]
        self.build(nums, 0, 0, self.n-1)

    def build(self, nums, i, left, right):
        if left == right:
            self.tree_max[i] = nums[left]
            self.tree_min[i] = nums[left]
        else:
            m = left + (right - left) // 2
            self.build(nums, i*2+1, left, m)
            self.build(nums, i*2+2, m+1, right)
            self.tree_max[i] = max(self.tree_max[i*2+1], self.tree_max[i*2+2])
            self.tree_min[i] = min(self.tree_min[i*2+1], self.tree_min[i*2+2])
    
    def query(self, start, end, i = 0, left = 0, right = None):
        if right is None: right = self.n-1
        if end < left or start > right: return math.inf, -math.inf
        if start <= left and right <= end: return self.tree_min[i], self.tree_max[i]
        m = left + (right - left) // 2
        mnl, mxl = self.query(start, end, i*2+1, left, m)
        mnr, mxr = self.query(start, end, i*2+2, m+1, right)
        return min(mnl, mnr), max(mxl, mxr)
    


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SegmentTree(nums)
        pq = []
        for l in range(n):
            mn, mx = st.query(l, n-1)
            heappush(pq, (mn - mx, l, n-1))
        
        result = 0
        while k:
            v, l, r = heappop(pq)
            result -= v
            if r-1 >= l:
                mn, mx = st.query(l, r-1)
                heappush(pq, (mn - mx, l, r-1))
            k -= 1
        return result
