class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor = [[0 for j in range(n+1)] for i in range(m+1)]
        pq = []
        for i in range(m):
            for j in range(n):
                xor[i+1][j+1] = xor[i][j+1] ^ xor[i+1][j] ^ xor[i][j] ^ matrix[i][j]
                heappush(pq, xor[i+1][j+1])
                if len(pq) > k:
                    heappop(pq)
        return pq[0]
