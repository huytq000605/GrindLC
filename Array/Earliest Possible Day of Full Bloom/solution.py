class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        new_plant = []
        for i in range(n):
            new_plant.append((growTime[i], plantTime[i]))
        new_plant.sort(key = lambda plant: (-plant[0], plant[1]))
        day = 0
        result = 0
        for plant in range(n):
            grow_time, plant_time = new_plant[plant]
            result = max(result, day + plant_time + grow_time)
            day += plant_time
        return result