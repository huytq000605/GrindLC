class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        for i, row in enumerate(mat):
            s = sum(row)
            heappush(pq, (-s, -i))
            if len(pq) > k:
                heappop(pq)
        result = []
        while pq:
            result.append(-heappop(pq)[1])
        return result[::-1]
