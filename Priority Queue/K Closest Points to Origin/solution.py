class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            heappush(heap, (-x**2 - y**2, x, y))
            if len(heap) > k:
                heappop(heap)

        result = []
        for distance, x, y in heap:
            result.append([x, y])

        return result
