class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(int)
        for v, w in items1:
            counter[v] += w
        for v, w in items2:
            counter[v] += w
        return sorted(counter.items())
