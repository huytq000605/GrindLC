class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        result = -math.inf
        for a in '01234':
            for b in '01234':
                if a == b: continue
                dq = deque()
                ca, cb = 0, 0
                seen = dict()
                dq.append((0, 0))
                for c in s:
                    if c == a: ca += 1
                    elif c == b: cb += 1
                    dq.append((ca, cb))
                    while len(dq) > k and \
                        ca > dq[0][0] and \
                        cb > dq[0][1]:
                        pca, pcb = dq.popleft()
                        key = (pca % 2, pcb % 2)
                        if key not in seen:
                            seen[key] = pca - pcb
                        seen[key] = min(seen[key], pca - pcb)
                    
                    seen_key = (1 - (ca % 2), (cb % 2))
                    if seen_key in seen:
                        result = max(result, ca - cb - seen[seen_key])

        return result
