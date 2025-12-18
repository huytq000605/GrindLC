class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @cache
        def dfs(i, txn_type, txn):
            if i >= len(prices):
                if txn_type == 0: return 0
                return -math.inf
            if txn_type == 0:
                return max(
                    dfs(i+1, 0, txn), 
                    dfs(i+1, 1, txn+1) + prices[i] if txn < k else 0,
                    dfs(i+1, 2, txn+1) - prices[i] if txn < k else 0
                )
            elif txn_type == 1:
                return max(
                    dfs(i+1, 1, txn), 
                    dfs(i+1, 0, txn) - prices[i] 
                )
            else:
                return max(
                    dfs(i+1, 2, txn),
                    dfs(i+1, 0, txn) + prices[i]
                )
        result = dfs(0, 0, 0)
        dfs.cache_clear()
        return result
