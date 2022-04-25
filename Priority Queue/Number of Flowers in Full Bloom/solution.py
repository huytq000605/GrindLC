class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flowers.sort()
        persons = sorted([(p, i) for i, p in enumerate(persons)])
        heap = []
        result = [0 for i in range(len(persons))]
        i = 0
        for start, j in persons:
            while i < len(flowers) and flowers[i][0] <= start:
                heappush(heap, flowers[i][1])
                i += 1

            while heap and heap[0] < start:
                heappop(heap)
            result[j] = len(heap)
        return result