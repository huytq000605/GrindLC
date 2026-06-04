class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        earliest_land = math.inf
        for i in range(len(ld)):
            earliest_land = min(earliest_land, ls[i] + ld[i])
        result = math.inf
        earliest_water = math.inf
        for i in range(len(ws)):
            earliest_water = min(earliest_water, ws[i] + wd[i])
            result = min(result, max(earliest_land, ws[i]) + wd[i])
        for i in range(len(ld)):
            result = min(result, max(ls[i], earliest_water) + ld[i])
        return result

        
        
