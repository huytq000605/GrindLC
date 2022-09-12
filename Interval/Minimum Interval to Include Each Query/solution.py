class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((query, i) for i, query in enumerate(queries))
        pq = []
        result = [-1 for i in range(len(queries))]

        i, n = 0, len(intervals)
        for query, idx in queries:
            while i < n and intervals[i][0] <= query:
                start, end = intervals[i]
                size = end - start + 1
                heappush(pq, (size, end))
                i += 1

            while pq and pq[0][1] < query:
                heappop(pq)

            if pq:
                result[idx] = pq[0][0]
        return result
