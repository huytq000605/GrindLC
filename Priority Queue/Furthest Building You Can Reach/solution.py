class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if ladders:
                    ladders -= 1
                    heappush(pq, diff)
                elif pq and pq[0] < diff and bricks >= pq[0]:
                    bricks -= heappop(pq)
                    heappush(pq, diff)
                elif bricks >= diff:
                    bricks -= diff
                else:
                    return i-1
        return n-1

