class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        ds = defaultdict(lambda: math.inf)
        pq = [(0, start[0], start[1])]
        ds[(target[0], target[1])] = abs(target[1] - start[1]) + abs(target[0] - start[0])
        special = defaultdict(list)
        for x1, y1, x2, y2, d in specialRoads:
            special[(x1, y1)].append((x2, y2, d))
        while pq:
            s, r, c = heappop(pq)
            if ds[(r, c)] < s:
                continue
            ds[(target[0], target[1])] = min(ds[(target[0], target[1])], abs(target[0] - r) + abs(target[1] - c) + s)
            if (r, c) in special:
                for nr, nc, d in special[(r, c)]:
                    if s + d < ds[(nr, nc)]:
                        ds[(nr, nc)] = s + d
                        heappush(pq, (s+d, nr, nc))
            for nr, nc, _, _, _ in specialRoads:
                d = abs(nr - r) + abs(nc - c)
                if s + d < ds[(nr, nc)]:
                    ds[(nr, nc)] = s + d
                    heappush(pq, (s + d, nr, nc))
        return ds[(target[0], target[1])]
