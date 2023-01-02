class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arr = [math.ceil(dist[i] / speed[i]) for i in range(n)]
        arr.sort()
        for monster_ith, monster_can_kill in enumerate(arr):
            if monster_ith + 1 > monster_can_kill:
                return monster_ith
        return n