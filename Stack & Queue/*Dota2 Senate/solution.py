class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == "D": d.append(i)
            else: r.append(i)
        while r and d:
            i1, i2 = r.popleft(), d.popleft()
            if i1 < i2: r.append(i1 + n)
            else: d.append(i2 + n)
        if r: return "Radiant"
        else: return "Dire"
        
