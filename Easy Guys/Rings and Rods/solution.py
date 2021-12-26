class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for i in range(10)]
        for i in range(0, len(rings), 2):
            rod = int(rings[i+1])
            rods[rod].add(rings[i])
        result = 0
        for rod in rods:
            if len(rod) == 3:
                result += 1
        return result