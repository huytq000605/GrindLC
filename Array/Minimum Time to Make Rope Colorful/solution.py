class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        prev = "#"
        max_cost = 0
        for i, color in enumerate(colors):
            cost = neededTime[i]
            if color == prev:
                result += min(max_cost, cost)
                max_cost = max(max_cost, cost)
            else:
                prev = color
                max_cost = cost
        return result
