class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        result = 0
        while len(sticks) > 1:
            s1, s2 = heappop(sticks), heappop(sticks)
            heappush(sticks, s1 + s2)
            result += s1 + s2
        return result
