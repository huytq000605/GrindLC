class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        pq = []
        for num in arr:
            bits = 0
            for bit in range(14):
                if (num >> bit) & 1:
                    bits += 1
            heappush(pq, (bits, num))
        result = []
        while pq:
            result.append(heappop(pq)[1])
        return result
