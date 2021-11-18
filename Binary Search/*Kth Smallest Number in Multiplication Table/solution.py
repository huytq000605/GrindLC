class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start = 1
        end = m * n
        def count(num):
            result = 0
            for row in range(1, m + 1):
                result += min(n, num // row)
            return result
            
        while start < end:
            mid = start + (end - start) // 2
            c = count(mid)
            if c >= k:
                end = mid
            else: # Too little numbers < mid => increase mid
                start = mid + 1
        return start