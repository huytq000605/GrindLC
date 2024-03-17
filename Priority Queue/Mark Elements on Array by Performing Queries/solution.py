class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)
        pq = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(pq)
        s = sum(nums)
        result = []
        marked = [0 for _ in range(n)]
        for i, k in queries:
            if not marked[i]:
                s -= nums[i]
            marked[i] = 1
            
            while k and pq:
                num, i = heappop(pq)
                if not marked[i]:
                    k -= 1
                    marked[i] = 1
                    s -= num
            result.append(s)
        return result
