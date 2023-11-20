class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = defaultdict(int)
        for s in garbage:
            for g in s:
                total[g] += 1
        result = sum(total.values())
        for i, s in enumerate(garbage):
            if i > 0:
                result += len(total) * travel[i-1]
            for g in s:
                total[g] -= 1
                if total[g] == 0:
                    total.pop(g)
        return result

