class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        pq = []
        for i, a in enumerate(arrays):
            heappush(pq, (-a[0], i))
            if len(pq) > 2:
                heappop(pq)
        
        result = -math.inf
        # pq[1] has min element
        # pq[0] has second min element
        for i, a in enumerate(arrays):
            if pq[1][1] != i:
                result = max(result, a[-1] + pq[1][0])
            else:
                result = max(result, a[-1] + pq[0][0])
        return result

