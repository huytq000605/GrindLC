class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = []
        for i in range(n):
            people.append((efficiency[i], speed[i]))

        people.sort(reverse = True)
        heap = []
        total = 0
        result = 0
        
        for i in range(n):
            eff, sp = people[i]
            heappush(heap, sp)
            total += sp
            while len(heap) > k:
                total -= heappop(heap)
            result = max(result, total * eff)
        
        return result % (10**9 + 7)