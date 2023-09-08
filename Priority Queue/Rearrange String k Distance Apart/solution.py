class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        counter = Counter(s)
        pq = []
        for c, freq in counter.items():
            heappush(pq, (-freq, c))
        pending = deque()
        
        result = ""
        while pq or pending:
            if pending and len(result) >= k and result[len(result) - k] == pending[0][1]:
                heappush(pq, pending.popleft())
            if not pq: return ""
            f, c = heappop(pq)
            f += 1
            result += c
            if f != 0:
                pending.append((f, c))
        if pending: return ""
        return result
            
                
