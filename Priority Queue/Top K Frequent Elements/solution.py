class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        counter = Counter(nums)
        for num, freq in counter.items():
            heappush(pq, (freq, num))
            if len(pq) > k:
                heappop(pq)
        return [num for freq, num in pq]        
