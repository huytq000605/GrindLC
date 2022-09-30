class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        xs = set([b[0] for b in buildings] + [b[1] for b in buildings])
        n = len(buildings)
        idx = 0
        pq = []
        result = []
        for x in sorted(xs):
            while idx < n and buildings[idx][0] <= x:
                l, r, h = buildings[idx]
                heappush(pq, (-h, r))
                idx += 1
            
            while pq and pq[0][1] <= x:
                heappop(pq)
            
            if not pq:
                result.append([x, 0])
            elif not result or result[-1][1] != -pq[0][0]:
                result.append([x, -pq[0][0]])
        return result
            
