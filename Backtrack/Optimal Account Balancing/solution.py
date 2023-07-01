class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        people = [0 for _ in range(12)]
        for u, v, a in transactions:
            people[u] -= a
            people[v] += a
        states = []
        for p in people:
            if p != 0:
                states.append(p)
        def dfs(i):
            while i < len(states) and states[i] == 0:
                i += 1
            if i >= len(states):
                return 0
            result = math.inf
            for j in range(i+1, len(states)):
                # pruning: only make transaction for different sign
                if states[i] * states[j] < 0:
                    states[j] += states[i]
                    result = min(result, 1 + dfs(i+1))
                    states[j] -= states[i]
            return result
        return dfs(0)
            
