class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        start = 0
        end = min(ranks) * (cars ** 2)
        while start < end:
            mid = start + (end - start) // 2
            can = 0
            for rank in ranks:
                can += math.floor(math.sqrt(mid // rank))
            if can >= cars:
                end = mid
            else:
                start = mid + 1
        return start
