class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cur = ""
        pq = []
        result = 0
        for i, color in enumerate(colors):
            if color != cur:
                pq = []
            cur = color
            heappush(pq, neededTime[i])
            if len(pq) > 1:
                result += heappop(pq)
        return result


