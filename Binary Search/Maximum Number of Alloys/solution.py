class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        # n = num of metals
        # k = machines
        result = 0
        # 100
        for machine in range(k):
            can_do = 1
            start = 0
            end = 10**9
            while start < end:
                can_do = start + math.ceil((end - start + 1) // 2)
                total_cost = 0
                for metal in range(n):
                    need = composition[machine][metal] * can_do - stock[metal]
                    if need > 0:
                            total_cost += cost[metal] * need
                if total_cost > budget:
                    end = can_do - 1
                else:
                    start = can_do
            result = max(result, start)
        return result
