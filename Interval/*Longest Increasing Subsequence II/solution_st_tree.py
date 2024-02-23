class SegmentTree:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.val = 0
        self.left, self.right = None, None

    def query(self, start, end):
        if start > self.end or end < self.start:
            return 0

        if start <= self.start and end >= self.end:
            return self.val

        self.down()
        return max(self.left.query(start, end), self.right.query(start, end))

    def update(self, start, end, val):
        if start > self.end or end < self.start:
            return
        if start <= self.start and end >= self.end:
            self.val = val
            return

        self.down()
        self.left.update(start, end, val)
        self.right.update(start, end, val)
        self.val = max(self.left.val, self.right.val)

    def down(self):
        if not self.left:
            mid = self.start + (self.end - self.start) // 2
            self.left = SegmentTree(self.start, mid)
            self.right = SegmentTree(mid + 1, self.end)

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # st.query(i, i) = LIS ends at number i
        # st.query(i, j) = max(LIS) ends at number from i to j
        st = SegmentTree(0, max(nums))
        for num in nums:
            cur_max = st.query(max(0, num - k), num - 1) + 1
            pre_max = st.query(num, num)
            st.update(num, num, max(cur_max, pre_max))
        return st.val
