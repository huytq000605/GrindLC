class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        seen = set([x])
        dq = deque([(x, 0)])
        while dq:
        # Divide x by 11 if x is a multiple of 11.
        # Divide x by 5 if x is a multiple of 5.
        # Decrement x by 1.
        # Increment x by 1.
            x, t = dq.popleft()
            if x == y:
                return t
            if x % 11 == 0 and x // 11 not in seen:
                seen.add(x//11)
                dq.append((x // 11, t + 1))
            if x % 5 == 0 and x // 5 not in seen:
                seen.add(x//5)
                dq.append((x // 5, t + 1))
            if x + 1 not in seen:
                seen.add(x+1)
                dq.append((x + 1, t + 1))
            if x - 1 not in seen:
                seen.add(x-1)
                dq.append((x - 1, t + 1))
        return -1
        
