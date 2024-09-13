class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        pq = []
        result = []
        for n, f in zip(nums, freq):
            counter[n] += f
            heappush(pq, (-counter[n], n))
            while pq and -counter[pq[0][1]] != pq[0][0]:
                heappop(pq)
            if not pq: result.append(0)
            else: result.append(-pq[0][0])
        return result
