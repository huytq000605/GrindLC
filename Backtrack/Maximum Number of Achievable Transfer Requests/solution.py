class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        result = 0
        for mask in range(1 << m):
            degree = [0 for i in range(n)]
            rq = 0
            for i in range(m):
                if (mask >> i) & 1 == 1:
                    rq += 1
                    u, v = requests[i]
                    degree[u] += 1
                    degree[v] -= 1
            valid = True
            for d in degree:
                if d != 0:
                    valid = False
                    break
            if valid:
                result = max(result, rq)
        return result