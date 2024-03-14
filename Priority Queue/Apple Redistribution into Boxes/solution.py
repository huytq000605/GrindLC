class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        pq = []
        s = 0
        for cap in capacity:
            s += cap
            heappush(pq, cap)
            while pq and s - pq[0] >= apples:
                s -= heappop(pq)
        return len(pq)
