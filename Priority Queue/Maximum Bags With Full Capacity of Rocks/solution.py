class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], add_rocks: int) -> int:
        remaining = [capacity[i] - rocks[i] for i in range(len(rocks))]
        heapify(remaining)
        result = 0
        while remaining:
            r = heappop(remaining)
            if add_rocks < r:
                return result
            else:
                result += 1
                add_rocks -= r
        return result