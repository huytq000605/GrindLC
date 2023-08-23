class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        pq = []
        for c, f in counter.items():
            heappush(pq, (-f, c))
        s = ""
        while pq:
            f1, c1 = heappop(pq)

            if s and c1 == s[-1]:
                if not pq: return ""
                f2, c2 = heappop(pq)
                heappush(pq, (f1, c1))
                s += c2
                if f2 + 1 != 0: heappush(pq, (f2 + 1, c2))      
            else:
                s += c1
                if f1 + 1 != 0: heappush(pq, (f1 + 1, c1))
        return s
