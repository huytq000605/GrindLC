class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1 for _ in range(len(queries))]
        remaining_queries = defaultdict(list)
        for query_idx, (a, b) in enumerate(queries):
            if a > b and heights[a] > heights[b]:
                result[query_idx] = a
            elif b > a and heights[b] > heights[a]:
                result[query_idx] = b
            elif a == b:
                result[query_idx] = a
            else:
                remaining_queries[max(a, b)].append((max(heights[a], heights[b]), query_idx))

        pq = []
        for i, height in enumerate(heights):
            while pq and height > pq[0][0]:
                result[heappop(pq)[1]] = i
            if i in remaining_queries:
                for max_height, query_idx in remaining_queries[i]:
                    heappush(pq, (max_height, query_idx))
        return result
        
        
