class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        pq = [-c for c in counter.values()]
        cooldown = []
        t = 0
        heapify(pq)
        while pq or cooldown:
            if not pq:
                t = cooldown[0][0]
            while cooldown and cooldown[0][0] <= t:
                heappush(pq, -heappop(cooldown)[1])
            c = -heappop(pq)
            c -= 1
            if c:
                heappush(cooldown, (t + n + 1, c))
            t += 1
        return t

