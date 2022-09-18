class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        start = 0
        end = n - 1
        # cond: n - mid >= citations[mid]
        while start < end:
            mid = (start + end) // 2
            if n - mid > citations[mid]:
                start = mid + 1
            else:
                end = mid
        if citations[start] >= n - start:
            return n - start
        return 0
