class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        work = sorted([(capital[i], profits[i]) for i in range(n)])
        can_work = []
        i = 0
        while k:
            while i < n and work[i][0] <= w:
                c, p = work[i]
                heappush(can_work, -p)
                i += 1
            if not can_work:
                break
            w -= heappop(can_work)
            k -= 1
        return w
