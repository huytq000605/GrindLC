class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        @cache
        def dfs(i):
            if i >= len(offers):
                return 0
            not_sell = dfs(i+1)
            
            start= i+1
            end = len(offers)
            while start < end:
                mid = start + (end - start) // 2
                if offers[mid][0] <= offers[i][1]:
                    start = mid + 1
                else:
                    end = mid
            
            sell = offers[i][2] + dfs(start)
            return max(not_sell, sell)
        return dfs(0)
