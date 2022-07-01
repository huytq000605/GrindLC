class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda box: box[1], reverse = True)
        result = 0
        for num, unit_per_box in boxTypes:
            take = min(num, truckSize)
            truckSize -= take
            result += take * unit_per_box
            if truckSize == 0:
                break
        return result
