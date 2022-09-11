class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # sum(speed) + min(efficency)
        MOD = 10**9 + 7
        engineers = [(speed[i], efficiency[i]) for i in range(n)]
        engineers.sort(key = lambda engineer: -engineer[1])
        pq = []
        total_speed = 0
        result = 0
        for s, e in engineers:
            heappush(pq, s)
            total_speed += s
            if len(pq) > k:
                total_speed -= heappop(pq)
            result = max(result, total_speed * e)
        return result % MOD
