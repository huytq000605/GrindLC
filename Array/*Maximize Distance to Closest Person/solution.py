class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        distances = []
        
        current = math.inf
        for i in range(n):
            if seats[i] == 1:
                distances.append(0)
                current = 0
            else:
                distances.append(current)
            current += 1
        
        current = math.inf
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                current = 0
                distances[i] = 0
            else:
                distances[i] = min(distances[i], current)
            current += 1
        
        return max(distances)
