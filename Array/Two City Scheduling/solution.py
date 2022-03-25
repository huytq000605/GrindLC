class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        result = sum(costs[i][0] for i in range(len(costs)))
        costs.sort(key = lambda cost: -cost[0] + cost[1])
        result += sum(-costs[i][0] + costs[i][1] for i in range(n))
        return result