class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        result = [0 for _ in range(len(people))]
        f = 0
        people = sorted([(p, i) for i, p in enumerate(people)])
        pq = []
        for p, i in people:
            while f < len(flowers) and flowers[f][0] <= p:
                heappush(pq, flowers[f][1])
                f += 1
            while pq and pq[0] < p:
                heappop(pq)
            result[i] = len(pq)
        return result
