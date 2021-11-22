class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        curr = capacity
        result = 0
        for i in range(n):
            curr -= plants[i]
            if i < n - 1 and curr < plants[i + 1]:
                result += (i+1) * 2
                curr = capacity
            result += 1
        return result