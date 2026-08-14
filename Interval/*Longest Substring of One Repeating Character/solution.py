class ST:
    def __init__(self, n):
        self.n = n
        self.tree = [None for _ in range(4*n)]
    
    def build(self, s, i = 0, tl = 0, tr = None):
        if tr == None: tr = self.n - 1
        if tl == tr:
            self.tree[i] = [s[tl], s[tl], 1, 1, 1, 1]
            return self.tree[i]
        tm = tl + (tr - tl) // 2
        llc, lrc, ll, lp, ls, lb = self.build(s, i*2+1, tl, tm)
        rlc, rrc, rl, rp, rs, rb = self.build(s, i*2+2, tm+1, tr)
        prefix = lp
        suffix = rs
        if llc == lrc and lrc == rlc and ll == lp:
            prefix = ll + rp
        if rrc == rlc and rlc == lrc and rl == rs:
            suffix = rl + ls
        best = max(lb, rb)
        if lrc == rlc:
            best = max(best, ls + rp)
        self.tree[i] = [llc, rrc, ll + rl, prefix, suffix, best]
        return self.tree[i]

    def query_longest(self):
        return self.tree[0][5]
    
    def update(self, idx, c, i = 0, tl = 0, tr = None):
        if tr == None: tr = self.n - 1
        if idx < tl or idx > tr: return self.tree[i]
        if tl == tr: 
            self.tree[i] = [c, c, 1, 1, 1, 1]
            return self.tree[i]
        
        tm = tl + (tr - tl) // 2
        llc, lrc, ll, lp, ls, lb = self.update(idx, c, i*2+1, tl, tm)
        rlc, rrc, rl, rp, rs, rb = self.update(idx, c, i*2+2, tm+1, tr)
        prefix = lp
        suffix = rs
        if llc == lrc and lrc == rlc and ll == lp:
            prefix = ll + rp
        if rrc == rlc and rlc == lrc and rl == rs:
            suffix = rl + ls
        best = max(lb, rb)
        if lrc == rlc:
            best = max(best, ls + rp)
        self.tree[i] = [llc, rrc, ll + rl, prefix, suffix, best]
        return self.tree[i]

class Solution:
    def longestRepeating(self, s: str, qcs: str, qis: List[int]) -> List[int]:
        n = len(s)
        st = ST(n)
        st.build(s)
        result = [0 for _ in range(len(qcs))]
        for i, (qc, qi) in enumerate(zip(qcs, qis)):
            st.update(qi, qc)
            result[i] = st.query_longest()
        return result
