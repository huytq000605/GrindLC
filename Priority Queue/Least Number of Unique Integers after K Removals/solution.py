class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        freqs = list(counter.values())
        heapify(freqs)
        while freqs and freqs[0] <= k:
            k -= heappop(freqs)
        return len(freqs)
            
