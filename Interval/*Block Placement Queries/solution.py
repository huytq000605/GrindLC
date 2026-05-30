class SegmentTree:
    def __init__(self, n):
        self.tree = [0 for _ in range(4*n)]
        self.n = n

    def query(self, start, end, i = 0, left = 0, right = None):
        if right is None: right = self.n - 1
        if end < left or start > right: return 0
        if start <= left and right <= end: return self.tree[i]
        mid = left + (right - left) // 2
        return max(
            self.query(start, end, i*2+1, left, mid),
            self.query(start, end, i*2+2, mid+1, right)
        )

    def update(self, pos, v, i = 0, left = 0, right = None):
        if right is None: right = self.n - 1
        if pos < left or pos > right: return
        if left == right and left == pos:
            self.tree[i] = v
            return
        mid = left + (right - left) // 2
        self.update(pos, v, i*2+1, left, mid)
        self.update(pos, v, i*2+2, mid+1, right)
        self.tree[i] = max(self.tree[i*2+1], self.tree[i*2+2])

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MX = max(q[1] for q in queries)
        # Segment Tree keeps track of the max segment from 0 to x
        st = SegmentTree(MX+1)
        from sortedcontainers import SortedSet
        obstacles = SortedSet([0, MX+1])
        result = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = obstacles.bisect(x)
                nxt = obstacles[i]
                prv = obstacles[i-1]
                obstacles.add(x)
                """
                When there is obstacle added at X
                Segment Tree needs to update 2 segments, [l, x] and [x, r]
                with l is obstacle before x, r is obstacle after x
                """ 
                st.update(nxt, nxt - x)
                st.update(x, x - prv)
            else:
                x, sz = q[1], q[2]
                mx = st.query(0, x)
                if sz <= mx:
                    result.append(True)
                    continue
                i = obstacles.bisect(x)
                """
                if x is not an obstacle
                Segment Tree will miss the segment [l, x]
                """
                if obstacles[i] != x and sz <= x - obstacles[i-1]:
                    result.append(True)
                else: result.append(False)
                
        return result
