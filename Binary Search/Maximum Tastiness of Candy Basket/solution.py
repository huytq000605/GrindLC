class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        start, end = 0, 10**9
        n = len(price)
        
        def valid(d):
            i = 0
            count = 1
            for j in range(1, n):
                if price[j] - price[i] >= d:
                    i = j
                    count += 1
            return count >= k
        
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if valid(mid):
                start = mid
            else:
                end = mid - 1
        return start
