class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fractions = []
        for i in range(n-1):
            heappush(fractions, (arr[i] / arr[-1], i, n-1))
        
        while k > 0:
            fraction, start, end = heappop(fractions)
            k -= 1
            if k == 0:
                return [arr[start], arr[end]]
            if end - 1 > start:
                heappush(fractions, (arr[start] / arr[end - 1], start, end - 1))
        
        return -1