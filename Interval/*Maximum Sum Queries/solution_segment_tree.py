class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.arr = [-math.inf for _ in range(4*n)]

    def query(self, l, r):
        return self._query(l, r, 0, 0, self.n - 1)
    
    def update(self, p, v):
        return self._update(p, p, 0, v, 0, self.n - 1)
    
    def _query(self, l, r, i, lt, rt):
        if l > rt or r < lt:
            return -math.inf
        if l <= lt and rt <= r:
            return self.arr[i]
        mt = lt + (rt - lt) // 2
        left = self._query(l, r, i*2+1, lt, mt)
        right = self._query(l, r, i*2+2, mt+1, rt)
        return max(left, right)
    
    def _update(self, l, r, i, v, lt, rt):
        if l > rt or r < lt:
            return
        if l <= lt and rt <= r:
            self.arr[i] = max(self.arr[i], v)
            return
        mt = lt + (rt - lt) // 2
        self._update(l, r, i*2+1, v, lt, mt)
        self._update(l, r, i*2+2, v, mt+1, rt)
        self.arr[i] = max(self.arr[i*2+1], self.arr[i*2+2])
    


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        nums = sorted([(nums1[i], nums2[i]) for i in range(n)])
        queries = sorted([(x, y, i) for i, (x,y) in enumerate(queries)])
        result = [-1 for _ in range(len(queries))]
        
        num2_values = sorted(set(nums2) | set(query[1] for query in queries))
        st = SegmentTree(len(num2_values))
        mapping = dict()
        for i, num2 in enumerate(num2_values):
            mapping[num2] = i
        idx = n-1
        for x, y, i in queries[::-1]:
            while idx >= 0 and nums[idx][0] >= x:
                num2 = nums[idx][1]
                s  = sum(nums[idx])
                st.update(mapping[num2], s)
                idx -= 1
            max_sum = st.query(mapping[y], len(num2_values) - 1)
            if max_sum != -math.inf:
                result[i] = max_sum
        return result
