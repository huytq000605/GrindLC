class SegmentTree:
    def __init__(self, n):
        self.tree = [0 for _ in range(4*n)]
        self.n = n
    
    def query(self, start, end, left = 0, right = -1, idx = 0):
        if right == -1: right = self.n - 1
        if end < left or start > right:
            return -math.inf

        if start <= left and right <= end:
            return self.tree[idx]
        
        mid = left + (right - left) // 2
        return max(self.query(start, end, left, mid, idx * 2 + 1), \
                self.query(start, end, mid + 1, right, idx * 2 + 2) )
        

    def update(self, start, end, val, left = 0, right = -1, idx = 0):
        if right == -1: right = self.n - 1
        if end < left or start > right:
            return
        if start <= left and right <= end:
            self.tree[idx] = max(self.tree[idx], val)
            return
        
        mid = left + (right - left) // 2
        self.update(start, end, val, left, mid, idx * 2 + 1)
        self.update(start, end, val, mid + 1, right, idx * 2 + 2)
        self.tree[idx] = max(self.tree[idx*2+1], self.tree[idx*2+2])

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        # store all vals
        vals = set()
        for i, num in enumerate(nums):
            vals.add(num - i)

        # compress vals
        vals = sorted(vals)
        val_to_idx = dict()
        idx = 0
        for val in vals:
            val_to_idx[val] = idx
            idx += 1

        # nums[i] - i >= nums[j] - j
        m = len(vals)
        result = -math.inf
        st = SegmentTree(m)
        for i, num in enumerate(nums):
            result = max(result, num)
            if num > 0:
                idx_st = val_to_idx[num - i]
                res = max(st.query(0, idx_st) + num, num)
                st.update(idx_st, idx_st, res)
                result = max(result, res)
        
        return result
