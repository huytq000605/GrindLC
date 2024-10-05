class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for i in range(4*(n))]

    def query(self, start, end, tree_start = 0, tree_end = -1, k = 0):
        if tree_end == -1:
            tree_end = self.n

        if start > tree_end or end < tree_start:
            return 0

        if start <= tree_start and end >= tree_end:
            return self.tree[k]

        mid = tree_start + (tree_end - tree_start) // 2
        return max(self.query(start, end, tree_start, mid, 2*k+1), self.query(start, end, mid + 1, tree_end, 2*k+2))

    def update(self, pos, val, tree_start = 0, tree_end = -1, k = 0):
        if tree_end == -1:
            tree_end = self.n
        if tree_end == tree_start:
            self.tree[k] = val
            return

        mid = tree_start + (tree_end - tree_start) // 2
        if pos <= mid:
            self.update(pos, val, tree_start, mid, 2*k+1)
        else:
            self.update(pos, val, mid+1, tree_end, 2*k+2)

        self.tree[k] = max(self.tree[2*k+1], self.tree[2*k+2])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # st.query(i, i) = LIS ends at number i
        # st.query(i, j) = max(LIS) ends at number from i to j
        st = SegmentTree(max(nums))
        result = 0
        for num in nums:
            cur_max = st.query(max(0, num - k), max(0, num - 1)) + 1
            pre_max = st.query(num, num)
            result = max(result, cur_max, pre_max)
            st.update(num, max(cur_max, pre_max))
        return result
