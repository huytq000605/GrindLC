class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage = list(map(Counter, garbage))
        result = 0
        for g in "PGM":
            t = 0
            for idx, house in enumerate(garbage):
                if house[g] > 0:
                    result += t
                    result += house[g]
                    t = 0
                if idx < len(travel):
                    t += travel[idx]
        return result
