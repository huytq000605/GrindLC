class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_deg = [0 for _ in range(n)]
        out_deg = [0 for _ in range(n)]
        for u, v in trust:
            out_deg[u-1] += 1
            in_deg[v-1] += 1
        for i in range(n):
            if out_deg[i] == 0 and in_deg[i] == n-1:
                return i+1
        return -1
            
