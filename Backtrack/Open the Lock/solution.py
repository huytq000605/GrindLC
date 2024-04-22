class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set()
        for deadend in deadends:
            t = ()
            for num in [int(c) for c in deadend]:
                t += (num,)
            deadends_set.add(t)
        if (0,0,0,0) in deadends_set: return -1
        seen = set()
        seen.add((0, 0, 0, 0))
        dq = deque([((0, 0, 0, 0), 0)])
        target = [int(target[i]) for i in range(4)]
        target = (target[0], target[1], target[2], target[3])
        while dq:
            cur, steps = dq.popleft()
            if cur == target: return steps
            for i in range(4):
                for change in [-1, 1]:
                    nxt = cur[:i] + ((cur[i] + change + 10) % 10,) + cur[i+1:]
                    if nxt not in deadends_set and nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, steps + 1))
        return -1
