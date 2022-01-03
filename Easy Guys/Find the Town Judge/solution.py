class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        give_trust = [0 for i in range(n)]
        be_trust  = [0 for i in range(n)]
        for u, v in trust:
            u, v = u-1, v-1
            give_trust[u] += 1
            be_trust[v] += 1
    
        for person in range(n):
            if give_trust[person] == 0 and be_trust[person] == n - 1:
                return person + 1
        return -1
