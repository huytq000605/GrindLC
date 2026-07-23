class ST:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0 for _ in range(4*self.n)]
        self.build(arr)
    
    def build(self, arr, i = 0, l = 0, r = None):
        if r == None: r = self.n-1
        if l == r:
            self.tree[i] = arr[l]
        else:
            m = l + (r - l) // 2
            self.build(arr, i*2+1, l, m)
            self.build(arr, i*2+2, m+1, r)
            self.tree[i] = max(self.tree[i*2+1], self.tree[i*2+2])

    def query(self, qs, qe, i = 0, l = 0, r = None):
        if r == None: r = self.n-1
        if qe < l or qs > r:
            return 0
        if qs <= l and qe >= r:
            return self.tree[i]
        m = l + (r - l) // 2
        return max(self.query(qs, qe, i*2+1, l, m), self.query(qs, qe, i*2+2, m+1, r))

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        segments = []
        i_to_s = [0 for _ in range(len(s))]
        start = 0
        ones = 0
        for i in range(len(s)):
            if s[i] != s[start]:
                segments.append((s[start], start, i-1))
                start = i
            i_to_s[i] = len(segments)
            ones += s[i] == '1'
        segments.append((s[start], start, len(s) - 1))
        st = ST([(segments[si-1][2] - segments[si-1][1] + 1) + (segments[si+1][2] - segments[si+1][1] + 1) if (c == '1' and si > 0 and si < len(segments)-1) else 0 for si, (c, i, j) in enumerate(segments)])
        result = []
        for i, j in queries:
            si = i_to_s[i]
            sj = i_to_s[j]
            if sj - si <= 1:
                result.append(ones)
                continue
            extend = st.query(si+2, sj-2)
            
            # left most and right most are duplicate
            if si+1 == sj-1 and segments[si+1][0] == '1':
                extend = max(extend, (segments[si][2] - i + 1) + (j - segments[sj][1] + 1))
            else:
                # left most
                if segments[si+1][0] == '1':
                    extend = max(extend, (segments[si][2] - i + 1) + (segments[si+2][2] - segments[si+2][1] + 1))
                # right most
                if segments[sj-1][0] == '1':
                    extend = max(extend, (segments[sj-2][2] - segments[sj-2][1] + 1) + (j - segments[sj][1] + 1))
            result.append(ones + extend)
        
        return result
