class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = Counter()
        for u, v in roads:
            counter[u] += 1
            counter[v] += 1
        result = 0
        for freq in sorted(counter.values(), reverse = True):
            result += freq * n
            n -= 1
        return result