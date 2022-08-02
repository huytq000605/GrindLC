class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for k, trim in queries:
            arr = [*nums]
            pq = []
            for i, num in enumerate(nums):
                arr[i] = int(num[-1 - trim+1:])
                heappush(pq, (-arr[i], -i))
                if len(pq) > k:
                    heappop(pq)
            result.append(-heappop(pq)[1])
        return result
