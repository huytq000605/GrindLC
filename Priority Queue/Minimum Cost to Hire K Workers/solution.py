class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        n = len(quality)
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i], wage[i]))
        workers.sort()
        team = []
        result = math.inf
        total_quality = 0
        for ratio, q, w in workers:
            heappush(team, -q)
            total_quality += q
            if len(team) > k:
                total_quality += heappop(team)
            # It doesn't matter if we dont take this worker
            # If we take => calculate
            # If we don't take => already calculate previous step
            if len(team) == k:
                result = min(result, total_quality * ratio)             
        return result
